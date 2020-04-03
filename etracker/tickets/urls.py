from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "tickets"

urlpatterns = [
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("home/", views.index, name="home"),
    path("tickets/", views.tickets, name="tickets"),
    path("new/", views.new_ticket, name="new"),
    path("<int:ticket_id>/edit/", views.edit_ticket, name="edit"),
    path("<int:ticket_id>/comment/", views.add_comment, name="comment"),
]
