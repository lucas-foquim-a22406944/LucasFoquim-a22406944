import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import TFC, Licenciatura

with open('data/tfcs_deisi_2024_2025.json', encoding='utf-8') as f:
    dados = json.load(f)

tfcs_importados = 0
tfcs_ignorados = 0

for item in dados['tfcs']:
    titulo = item.get('titulo', '')
    ano = int(item.get('ano', 0))
    autores = item.get('autores', [])
    autor = ', '.join(autores) if autores else 'Desconhecido'
    url_repositorio = item.get('link_pdf', '')
    rating = item.get('rating', 0)
    destaque = rating >= 4  # TFCs com rating 4 ou 5 ficam em destaque

    nome_licenciatura = item.get('licenciatura', '')
    licenciatura_obj = Licenciatura.objects.filter(nome__icontains=nome_licenciatura).first()

    tfc, criado = TFC.objects.get_or_create(
        titulo=titulo,
        defaults={
            'autor': autor,
            'ano': ano,
            'url_repositorio': url_repositorio,
            'destaque': destaque,
            'licenciatura': licenciatura_obj,
        }
    )

    if criado:
        tfcs_importados += 1
        print(f"[OK] Importado: {titulo}")
    else:
        tfcs_ignorados += 1
        print(f"[SKIP] Já existe: {titulo}")

print(f"\nConcluído! {tfcs_importados} importados, {tfcs_ignorados} já existiam.")