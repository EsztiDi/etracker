from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
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

class UserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name", )
