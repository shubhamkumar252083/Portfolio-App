from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "technology")
    search_fields = ("id", "title", "description", "technology")


admin.site.register(Project, ProjectAdmin)
