from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Ticket, Comment


@login_required
def index(request):
    tickets = Ticket.objects.all().order_by("-date_added")
    fields = Ticket._meta.get_fields()
    # {{field.verbose_name.title}}
    context = {"tickets": tickets, "fields": fields}
    return render(request, "tickets/index.html", context)
