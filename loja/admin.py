from django.contrib import admin

# Register your models here.
from .models import Loja

class LojaAdmin(admin.ModelAdmin):
    list_display = ("nome", "produtos",)
    ordering = ("nome", "produtos",)
    search_fields = ("nome",)



admin.site.register(Loja, LojaAdmin)