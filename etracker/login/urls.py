from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "login"

urlpatterns = [
    path("", LoginView.as_view(template_name="login/index.html"))
    #views.index, name="index"),
]
