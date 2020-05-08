from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Ticket, Comment


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("status", "priority", "assignee", "description", "details", )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(TicketForm, self).__init__(*args, **kwargs)
        group_name = user.groups.values_list("name", flat=True).first()
        self.fields["assignee"].queryset = User.objects.filter(groups__name__contains=group_name)
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", )

class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name", )

