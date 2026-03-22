from django.contrib import admin

# Register your models here.
from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cidade",)
    ordering = ("nome", "cidade",)
    search_fields = ("nome",)



admin.site.register(Escola, EscolaAdmin)