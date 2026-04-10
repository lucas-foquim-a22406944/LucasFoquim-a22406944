import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular, Docente

PASTA_JSONS = 'data'
course = 260
language = 'PT'

ficheiro_curso = os.path.join(PASTA_JSONS, f'ULHT{course}-{language}.json')

if not os.path.exists(ficheiro_curso):
    print(f"[ERRO] Ficheiro não encontrado: {ficheiro_curso}")
    exit()

with open(ficheiro_curso, encoding='utf-8') as f:
    course_data = json.load(f)

print("JSON do curso carregado com sucesso!")

licenciatura_obj, criada = Licenciatura.objects.get_or_create(
    nome='Licenciatura em Engenharia Informática',
    defaults={
        'instituicao': 'Universidade Lusófona',
        'grau': 'Licenciatura',
        'area': 'Engenharia Informática',
        'duracao_anos': 3,
        'ano_inicio': 2022,
    }
)
if criada:
    print("[OK] Licenciatura criada!")
else:
    print("[SKIP] Licenciatura já existe.")

# Apagar UCs sem nome que ficaram da tentativa anterior
UnidadeCurricular.objects.filter(nome='').delete()
print("[OK] UCs sem nome removidas.")

ucs_importadas = 0
ucs_ignoradas = 0

for uc in course_data.get('courseFlatPlan', []):
    nome_uc = uc.get('curricularUnitName', '')  # campo correto
    ano_curricular = uc.get('curricularYear', 1)
    semestre_codigo = uc.get('semesterCode', 'S')
    ects = uc.get('ects', 0) or 0
    codigo = uc.get('curricularIUnitReadableCode', '')

    # Converter semestre: S1=1, S2=2, S=1 (semestral genérico)
    if semestre_codigo == 'S1':
        semestre = 1
    elif semestre_codigo == 'S2':
        semestre = 2
    else:
        semestre = 1

    if not nome_uc:
        print(f"[AVISO] UC sem nome ignorada: {codigo}")
        continue

    ficheiro_uc = os.path.join(PASTA_JSONS, f'{codigo}-{language}.json')
    uc_data = {}
    if os.path.exists(ficheiro_uc):
        with open(ficheiro_uc, encoding='utf-8') as f:
            uc_data = json.load(f)
    else:
        print(f"[AVISO] JSON da UC não encontrado: {ficheiro_uc}")

    uc_obj, criada = UnidadeCurricular.objects.get_or_create(
        nome=nome_uc,
        defaults={
            'ano_curricular': ano_curricular,
            'semestre': semestre,
            'ects': int(ects),
        }
    )

    uc_obj.licenciatura.add(licenciatura_obj)

    for docente in uc_data.get('teachers', []):
        nome_docente = docente.get('name', '')
        url_perfil = docente.get('profileUrl', '')
        if nome_docente:
            docente_obj, _ = Docente.objects.get_or_create(
                nome=nome_docente,
                defaults={'url_perfil': url_perfil}
            )
            uc_obj.docentes.add(docente_obj)

    if criada:
        ucs_importadas += 1
        print(f"[OK] Importada: {nome_uc}")
    else:
        ucs_ignoradas += 1
        print(f"[SKIP] Já existe: {nome_uc}")

print(f"\nConcluído! {ucs_importadas} UCs importadas, {ucs_ignoradas} já existiam.")