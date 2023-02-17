from django.urls import path, include

from . import views


urlpatterns = [
    path("add_quarto", views.add_quarto),
    path("list_quartos", views.list_quartos),
]
