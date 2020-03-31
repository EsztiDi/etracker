from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, Comment


@login_required
def index(request):
    all_tickets = Ticket.objects.all().order_by("-date_added")
    my_tickets = request.user.my_tickets.all().order_by("-priority", "-date_added")
    assigned_tickets = request.user.assigned_tickets.all().order_by("-priority",
                                                                    "-date_added")
    unassigned = Ticket.objects.filter(assignee=None).order_by("-date_added")
    new_tickets = Ticket.objects.filter(status=1).order_by("-date_added")
    context = {"all_tickets": all_tickets, "my_tickets": my_tickets,
               "assigned_tickets": assigned_tickets, "unassigned": unassigned, "new_tickets": new_tickets}
    return render(request, "tickets/index.html", context)

    # fields = Ticket._meta.get_fields()
    # {{field.verbose_name.title}}
