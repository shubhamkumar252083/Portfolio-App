from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("rough/", include("rough.urls")),
    path('admin/', admin.site.urls),
    path("projects/", include("projects.urls")),
    path("blog/", include("blog.urls")),
]
