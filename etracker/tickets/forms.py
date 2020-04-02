from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("status", "priority", "assignee", "description", "details", )


class EditForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("status", "priority", "assignee", )
