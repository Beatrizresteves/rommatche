from django.urls import path, include

from . import views


urlpatterns = [
    path("addQuarto", views.add_quarto),
    path("listQuartos", views.list_quartos),
]
