from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("projects.urls")),
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("contactMe/", include("contactMe.urls")),
]
