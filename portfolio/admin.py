from django.contrib import admin

# Register your models here.

from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Competencia, Projeto, Formacao, TFC, MakingOf

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'instituicao', 'grau', 'area', 'ano_inicio', 'duracao_anos')
    search_fields = ('nome', 'instituicao', 'area')


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'departamento', 'url_perfil')
    search_fields = ('nome', 'email', 'departamento')


@admin.register(UnidadeCurricular)
class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_curricular', 'semestre', 'ects')
    list_filter = ('ano_curricular', 'semestre')
    search_fields = ('nome',)
    filter_horizontal = ('licenciatura', 'docentes')


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel_interesse')
    list_filter = ('tipo', 'nivel_interesse')
    search_fields = ('nome', 'descricao')


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel')
    list_filter = ('tipo', 'nivel')
    search_fields = ('nome', 'descricao')
    filter_horizontal = ('tecnologias',)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'unidade_curricular', 'url_github')
    list_filter = ('ano', 'unidade_curricular')
    search_fields = ('titulo', 'descricao', 'conceitos_aplicados')
    filter_horizontal = ('tecnologias', 'competencias')


@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'tipo', 'data_inicio', 'data_fim')
    list_filter = ('tipo', 'data_inicio')
    search_fields = ('titulo', 'instituicao', 'descricao')
    filter_horizontal = ('competencias',)


@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano', 'destaque', 'licenciatura')
    list_filter = ('ano', 'destaque', 'licenciatura')
    search_fields = ('titulo', 'autor')


@admin.register(MakingOf)
class MakingOfAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fase', 'entidade_relacionada', 'data')
    list_filter = ('fase',)
    search_fields = ('titulo', 'descricao', 'entidade_relacionada')