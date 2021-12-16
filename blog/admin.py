from django.contrib import admin
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    # note "list_display" & "search_fields" elements must not be "ManyToMany" like "categories"
    list_display = ("title", "id")
    search_fields = ("id", "title")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("id", "name")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "created_on", "post")
    search_fields = ("id", "author", "created_on")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
