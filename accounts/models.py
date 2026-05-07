from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    token = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"