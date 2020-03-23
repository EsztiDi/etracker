from django.urls import path
from . import views

app_name = "tickets"

urlpatterns = [
    path("home/", views.index, name="home")
]
