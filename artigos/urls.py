from django.urls import path
from . import views

urlpatterns = [
    path('', views.artigos_view, name='artigos'),
    path('<int:id>/', views.artigo_view, name='artigo'),
    path('novo/', views.artigo_criar, name='artigo_criar'),
    path('<int:id>/editar/', views.artigo_editar, name='artigo_editar'),
    path('<int:id>/apagar/', views.artigo_apagar, name='artigo_apagar'),
]