from django.contrib import admin

from .models import ContactMe


class ContactMeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "ph_no")
    search_fields = ("id", "name", "email", "ph_no")


admin.site.register(ContactMe, ContactMeAdmin)
