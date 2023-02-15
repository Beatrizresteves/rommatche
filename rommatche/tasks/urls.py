from django.urls import path, include

from . import views


urlpatterns = [
    path("add", views.add_todo),
    path("list", views.list_todos),
]
