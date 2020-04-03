from django import forms
from .models import Ticket, Comment


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("status", "priority", "assignee", "description", "details", )


class EditForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ("status", "priority", "assignee", )
    

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("text", )
