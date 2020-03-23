from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.utils import timezone
from .models import Ticket, Comment

admin.site.site_header = "ETracker Admin"
admin.site.site_title = "ETracker Admin"
admin.site.index_title = "Welcome to the ETracker admin area!"


class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "ticket", "commenter", "date", )
    fields = ("ticket", "text", )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.commenter = request.user
        super().save_model(request, obj, form, change)


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ("text", "commenter", "date", )
    readonly_fields = ("text", "commenter", "date", )
    classes = ("collapse", )
    extra = 0


class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "status", "priority",
                    "added_by", "assignee", "date_updated", "date_added", )
    list_display_links = ("description", )
    list_filter = ("priority", "status", )
    fields = ("status", "priority", "assignee", "description", "details", )
    inlines = (CommentInline, )
    search_fields = ("id", "description", "details",
                     "added_by__username", "assignee__username", )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.added_by = request.user
        elif change:
            obj.date_updated = timezone.now()
        super().save_model(request, obj, form, change)


class CustomUserAdmin(UserAdmin):

    def save_model(self, request, obj, form, change):
        if "is_active" in form.changed_data:
            Ticket.objects.filter(assignee_id=obj.id).update(assignee=None)
        super(CustomUserAdmin, self).save_model(request, obj, form, change)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment, CommentAdmin)
