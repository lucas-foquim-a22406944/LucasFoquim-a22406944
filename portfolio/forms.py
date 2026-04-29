from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'ano', 'imagem', 'url_github', 'url_video', 'conceitos_aplicados', 'unidade_curricular', 'tecnologias', 'competencias']

class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = ['nome', 'tipo', 'logo', 'url_site', 'nivel_interesse', 'descricao']

class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = ['nome', 'tipo', 'descricao', 'nivel', 'tecnologias']

class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = ['titulo', 'instituicao', 'data_inicio', 'data_fim', 'descricao', 'certificado_url', 'tipo', 'competencias']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
        }