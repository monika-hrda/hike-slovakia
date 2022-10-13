from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'contact_email',
        'subject',
        'message',
        'creation_date',
    )


admin.site.register(Contact, ContactAdmin)
