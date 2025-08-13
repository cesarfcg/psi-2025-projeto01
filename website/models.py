from django.db import models

# Create your models here.
class Jogador(models.Model):
    POSICOESCHOICE = [        ("GOL", "Goleiro"),
        ("ZAG", "Zagueiro"),
        ("LAT", "Lateral"),
        ("VOL", "Volante"),
        ("MEI", "Meia"),
        ("ATA", "Atacante"),
        ("TEC", "Treinador"),
    ]
    nome_camisa = models.CharField( max_length=50)
    nome_completo = models.CharField( max_length=100)
    nome_camisa = models.CharField( max_length=50)
    posicao = models.CharField( choices=POSICOESCHOICE, default="Atacante")
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    local_nascimento = models.CharField( max_length=50)
    nacionalidade = models.CharField( max_length=50)
    imagem = models.ImageField(upload_to="jogadores/",blank=True)
class Jogo(models.Model):
    CAMPEONATOCHOICE = (("BRASILEIRÃO","Brasileirão"), ("LIBERTADORES","Libertadores"),)

    data = models.DateField()
    campeonato =  models.CharField(choices=CAMPEONATOCHOICE, default="Amistoso")
    estadio = models.CharField()
    time_casa = models.CharField() 
    time_visitante = models.CharField() 
    placar_casa = models.IntegerField(blank=True)
    placar_visitante = models.IntegerField(blank=True)

class ProximoJogo(models.Model):
    CAMPEONATOCHOICE = (("BRASILEIRÃO","Brasileirão"), ("LIBERTADORES","Libertadores"),)

    data = models.DateField()
    campeonato =  models.CharField(choices=CAMPEONATOCHOICE, default="Amistoso")
    estadio = models.CharField()
    time_casa = models.CharField() 
    time_visitante = models.CharField() 
    

class Noticia(models.Model):
    titulo = models.CharField( max_length=50)
    data = models.DateField()
    resumo = models.TextField()
    imagem = models.ImageField(upload_to="noticias/",blank=True)

        
class Introducao(models.Model):
    introducao = models.TextField()
class Sobre(models.Model):
    sobre = models.TextField()
class Autor(models.Model):
    nome = models.CharField(max_length=80)
    email = models.EmailField( max_length=254)
class Credito(models.Model):
    credito = models.TextField()