from django.db import models

# Create your models here.from django.db import models


class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    grau = models.CharField(max_length=100)
    area = models.CharField(max_length=200)
    duracao_anos = models.IntegerField()
    ano_inicio = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - {self.instituicao}"


class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    url_perfil = models.URLField(blank=True)
    departamento = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    SEMESTRE_CHOICES = [
        (1, '1º Semestre'),
        (2, '2º Semestre'),
    ]

    nome = models.CharField(max_length=200)
    ano_curricular = models.IntegerField()
    semestre = models.IntegerField(choices=SEMESTRE_CHOICES)
    ects = models.IntegerField()
    licenciatura = models.ManyToManyField(Licenciatura, related_name='unidades_curriculares')
    docentes = models.ManyToManyField(Docente, related_name='unidades_curriculares', blank=True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    TIPO_CHOICES = [
    ('linguagem', 'Linguagem'),
    ('framework', 'Framework'),
    ('ferramenta', 'Ferramenta'),
    ('base_dados', 'Base de Dados'),
    ('frontend', 'Frontend'),
    ('backend', 'Backend'),
    ('storage', 'Storage'),
    ('outro', 'Outro'),
]
    NIVEL_CHOICES = [
        (1, ' Iniciante'),
        (2, ' Básico'),
        (3, ' Intermédio'),
        (4, ' Avançado'),
        (5, ' Expert'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    logo = models.ImageField(upload_to='tecnologias/', blank=True)
    url_site = models.URLField(blank=True)
    nivel_interesse = models.IntegerField(choices=NIVEL_CHOICES, default=3)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome



class Competencia(models.Model):
    TIPO_CHOICES = [
        ('tecnica', 'Técnica'),
        ('soft', 'Soft Skill'),
        ('linguistica', 'Linguística'),
    ]

    NIVEL_CHOICES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermédio'),
        ('avancado', 'Avançado'),
    ]

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    descricao = models.TextField(blank=True)
    nivel = models.CharField(max_length=50, choices=NIVEL_CHOICES, default='intermedio')
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias', blank=True)

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ano = models.IntegerField()
    imagem = models.ImageField(upload_to='projetos/', blank=True)
    url_github = models.URLField(blank=True)
    url_video = models.URLField(blank=True)
    conceitos_aplicados = models.TextField(blank=True)
    unidade_curricular = models.ForeignKey(
        UnidadeCurricular,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='projetos'
    )
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos', blank=True)
    competencias = models.ManyToManyField(Competencia, related_name='projetos', blank=True)

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    TIPO_CHOICES = [
        ('online', 'Online'),
        ('presencial', 'Presencial'),
        ('academico', 'Académico'),
    ]

    titulo = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)  # adicionar esta linha
    certificado_url = models.URLField(blank=True)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, default='online')
    competencias = models.ManyToManyField(Competencia, related_name='formacoes', blank=True)

    class Meta:
        ordering = ['-data_inicio']

    def __str__(self):
        return f"{self.titulo} - {self.instituicao}"


class TFC(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.CharField(max_length=200)
    ano = models.IntegerField()
    destaque = models.BooleanField(default=False)
    url_repositorio = models.URLField(blank=True)
    licenciatura = models.ForeignKey(
        Licenciatura,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='tfcs'
    )

    def __str__(self):
        return f"{self.titulo} ({self.ano})"


class MakingOf(models.Model):
    FASE_CHOICES = [
        ('modelacao', 'Modelação'),
        ('implementacao', 'Implementação'),
        ('testes', 'Testes'),
        ('revisao', 'Revisão'),
    ]

    titulo = models.CharField(max_length=200)
    data = models.DateField(auto_now_add=True)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='makingof/', blank=True)
    fase = models.CharField(max_length=50, choices=FASE_CHOICES, default='modelacao')
    entidade_relacionada = models.CharField(max_length=100, blank=True)
    uso_ia = models.TextField(blank=True, help_text='Descreve como usaste IA (se aplicável)')

    class Meta:
        ordering = ['-data']
        verbose_name_plural = 'Making Of'

    def __str__(self):
        return f"{self.titulo} ({self.fase})"
