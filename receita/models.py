from django.db import models

# Create your models here.
class Receita(models.Model):
    nome = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.nome} feita com : {self.ingredientes}'