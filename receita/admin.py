from django.contrib import admin

# Register your models here.
from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("nome", "ingredientes",)
    ordering = ("nome", "ingredientes",)
    search_fields = ("nome",)



admin.site.register(Receita, ReceitaAdmin)