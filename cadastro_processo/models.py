from django.db import models

class Planilha(models.Model):
    nome = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    arquivo = models.FileField()
    
