from django.contrib import admin

# Register your models here.
from home.models import Settings, ContactFormMessage, UserProfile, Faq


class contact_form_message_admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'ip', 'status', 'note']
    list_filter = ['status']


class user_profile_admin(admin.ModelAdmin):
    list_display = ['full_name', 'user_name', 'phone', 'address', 'city', 'country', 'image', 'get_image_tag']


class faq_admin(admin.ModelAdmin):
    list_display = ['order_faq', 'question', 'answer', 'status']
    list_filter = ['status']


admin.site.register(Settings)
admin.site.register(UserProfile, user_profile_admin)
admin.site.register(ContactFormMessage, contact_form_message_admin)
admin.site.register(Faq, faq_admin)
