from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("login/", admin.site.urls), 
    path("keeps/", include("keeps.urls")),
    path("tasks/", include("tasks.urls")),
    path("contacts/", include("contacts.urls")),
]