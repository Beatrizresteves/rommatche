from django.contrib import admin

from .models import Quarto
# Register your models here.


class QuartosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'valor', 'description', 'imagem')


admin.site.register(Quarto, QuartosAdmin)
