from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage


class contact_form_message_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'ip', 'status', 'note']
    list_filter = ['status']

admin.site.register(Settings)
admin.site.register(ContactFormMessage, contact_form_message_admin)
