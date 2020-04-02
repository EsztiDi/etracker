from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils import timezone
from .models import Ticket, Comment
from .forms import TicketForm, EditForm


@login_required
def index(request):
    my_tickets = request.user.my_tickets.exclude(status=4).order_by("-priority", "-date_added")
    assigned_tickets = request.user.assigned_tickets.exclude(status=4).order_by("-priority",
                                                                    "-date_added")
    unassigned = Ticket.objects.filter(assignee=None).exclude(status=4).order_by("-date_added")
    new_tickets = Ticket.objects.filter(status=1).order_by("-date_added")
    
    context = {"my_tickets": my_tickets,
               "assigned_tickets": assigned_tickets, "unassigned": unassigned, "new_tickets": new_tickets}

    return render(request, "tickets/index.html", context)

    # fields = Ticket._meta.get_fields()
    # {{field.verbose_name.title}}


@login_required
def tickets(request):
    all_tickets = Ticket.objects.all().order_by("-date_added")
    return render(request, "tickets/tickets.html", {"all_tickets": all_tickets})


@login_required
def new_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.added_by = request.user
            new.save()
            return redirect("/tickets/")
    else:
        form = TicketForm()
    return render(request, "tickets/new_ticket.html", {"form": form})


@login_required
@xframe_options_sameorigin
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        edit_form = TicketForm(request.POST, instance=ticket)
        if edit_form.is_valid() and edit_form.has_changed():
            ticket = edit_form.save(commit=False)
            ticket.date_updated = timezone.now()
            ticket.save()
    else:
        edit_form = TicketForm(instance=ticket)
    return render(request, "tickets/edit_ticket.html", {"edit_form": edit_form})
