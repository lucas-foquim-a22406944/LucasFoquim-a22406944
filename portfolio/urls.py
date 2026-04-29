from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='portfolio_index'),

    # Sobre
    path('sobre/', views.sobre_view, name='sobre'),

    # Projetos
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/novo/', views.projeto_criar, name='projeto_criar'),
    path('projeto/<int:id>/editar/', views.projeto_editar, name='projeto_editar'),
    path('projeto/<int:id>/apagar/', views.projeto_apagar, name='projeto_apagar'),

    # Tecnologias
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('tecnologia/nova/', views.tecnologia_criar, name='tecnologia_criar'),
    path('tecnologia/<int:id>/editar/', views.tecnologia_editar, name='tecnologia_editar'),
    path('tecnologia/<int:id>/apagar/', views.tecnologia_apagar, name='tecnologia_apagar'),

    # Competencias
    path('competencias/', views.competencias_view, name='competencias'),
    path('competencia/nova/', views.competencia_criar, name='competencia_criar'),
    path('competencia/<int:id>/editar/', views.competencia_editar, name='competencia_editar'),
    path('competencia/<int:id>/apagar/', views.competencia_apagar, name='competencia_apagar'),

    # Formacoes
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('formacao/nova/', views.formacao_criar, name='formacao_criar'),
    path('formacao/<int:id>/editar/', views.formacao_editar, name='formacao_editar'),
    path('formacao/<int:id>/apagar/', views.formacao_apagar, name='formacao_apagar'),
]