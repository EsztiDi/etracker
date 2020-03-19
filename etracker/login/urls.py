from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = "login"

urlpatterns = [
    path("", LoginView.as_view(template_name="login/index.html"), name="login"),
]
