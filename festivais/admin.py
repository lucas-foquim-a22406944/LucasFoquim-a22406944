from django.contrib import admin

# Register your models here.
from .models import Festivais

class FestivaisAdmin(admin.ModelAdmin):
    list_display = ("nome", "zona",)
    ordering = ("nome", "zona",)
    search_fields = ("nome",)



admin.site.register(Festivais, FestivaisAdmin)