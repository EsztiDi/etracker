from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
# Remove in production:
from django.conf import settings
from django.conf.urls.static import static

app_name = "tickets"

urlpatterns = [
    path("", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.logout_then_login, name="logout"),
    path("home/", views.index, name="home"),
    path("tickets/", views.tickets, name="tickets"),
    path("ticket/new/", views.new_ticket, name="new"),
    path("ticket/<int:ticket_id>/watch/", views.watch_ticket, name="watch"),
    path("ticket/<int:ticket_id>/edit/", views.edit_ticket, name="edit"),
    path("ticket/<int:ticket_id>/comment/", views.add_comment, name="comment"),
    path("ticket/<int:ticket_id>/delete/", views.delete_ticket, name="delete_ticket"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
    path("account/", views.account, name="account"),
    path("change-password/", views.change_password, name="change_password"),
    path("cookie-policy/", views.cookie_policy, name="cookies"),
    path("favicon.ico/", RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico")), name="favicon"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Remove in production
