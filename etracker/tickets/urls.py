from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "tickets"

urlpatterns = [
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("home/", views.index, name="home"),
    path("new/", views.new_ticket, name="new"),
    path("tickets/", views.tickets, name="tickets"),
]
