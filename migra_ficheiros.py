import os
from django.core.files import File
from portfolio.models import Projeto, Tecnologia
from artigos.models import Artigo

# Migrar imagens dos Projetos
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Projeto migrado: {obj}")

# Migrar logos das Tecnologias
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join('media', obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Tecnologia migrada: {obj}")

# Migrar fotografias dos Artigos
for obj in Artigo.objects.all():
    if obj.fotografia and obj.fotografia.name:
        local_path = os.path.join('media', obj.fotografia.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(os.path.basename(local_path), File(f), save=True)
            print(f"Artigo migrado: {obj}")

from portfolio.models import MakingOf

# Migrar imagens do MakingOf
for obj in MakingOf.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"MakingOf migrado: {obj}")

print("Migração concluída!")