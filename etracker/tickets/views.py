from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone
from .models import Ticket, Comment
from django.contrib.auth.forms import PasswordChangeForm
from .forms import TicketForm, CommentForm, UserForm


@login_required
def index(request):
    my_tickets = request.user.my_tickets.exclude(status=4).order_by("-priority")
    assigned_tickets = request.user.assigned_tickets.exclude(status=4).order_by("-priority")
    unassigned = Ticket.objects.filter(assignee=None).exclude(status=4)
    new_tickets = Ticket.objects.filter(status=1)
    watched_tickets = request.user.watched_tickets.exclude(status=4)
    all_tickets = Ticket.objects.all()

    context = {"my_tickets": my_tickets,
               "assigned_tickets": assigned_tickets, 
               "unassigned": unassigned, 
               "new_tickets": new_tickets,
               "watched_tickets": watched_tickets,
               "all_tickets": all_tickets}

    return render(request, "tickets/index.html", context)


@login_required
def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, "tickets/tickets.html", {"all_tickets": all_tickets})


@login_required
def watch_ticket(request, ticket_id):
    redirect_to = request.GET.get("next", "/home/")
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.user in ticket.watchers.all():
        ticket.watchers.remove(request.user)
    else:
        ticket.watchers.add(request.user)
    return HttpResponseRedirect(redirect_to)


@login_required
def new_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.added_by = request.user
            new.save()
            return redirect("/home/")
    else:
        form = TicketForm()
    return render(request, "tickets/new_ticket.html", {"form": form})


@login_required
@xframe_options_sameorigin
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == "POST":
        edit_form = TicketForm(request.POST, instance=ticket)
        if edit_form.is_valid() and edit_form.has_changed():
            ticket = edit_form.save(commit=False)
            ticket.date_updated = timezone.now()
            ticket.save()
    else:
        edit_form = TicketForm(instance=ticket)
    return render(request, "tickets/edit_ticket.html", {"edit_form": edit_form})


@login_required
@xframe_options_sameorigin
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.ticket = ticket
            comment.commenter = request.user
            comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request, "tickets/add_comment.html", {"comment_form": comment_form})


@login_required
def delete_ticket(request, ticket_id):
    redirect_to = request.GET.get("next", "/home/")
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    ticket.delete()
    return HttpResponseRedirect(redirect_to)


@login_required
def delete_comment(request, comment_id):
    redirect_to = request.GET.get("next", "/home/")
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return HttpResponseRedirect(redirect_to)

@login_required
def account(request):
    if request.method == "POST":
        settings_form = UserForm(request.POST, instance=request.user)
        if settings_form.is_valid():
            new_settings = settings_form.save()
            update_session_auth_hash(request, new_settings)
            messages.success(request, "Your details were successfully updated.")
    else:
        settings_form = UserForm(instance=request.user)
    return render(request, "tickets/account.html", {"settings_form": settings_form})


@login_required
@xframe_options_sameorigin
def change_password(request):
    if request.method == "POST":
        change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if change_form.is_valid():
            change_form.save()
            update_session_auth_hash(request, change_form.user)
            messages.success(request, "Your password was successfully updated.")
    else:
        change_form = PasswordChangeForm(user=request.user)
    
    for field in change_form.fields.values():
        field.help_text = None
        
    return render(request, "registration/change_password.html", {"change_form": change_form})


def cookie_policy(request):
    return render(request, "tickets/cookie_policy.html")
