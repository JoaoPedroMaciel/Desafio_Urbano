from django.db import models

class Processo(models.Model):
    pasta = models.CharField(max_length=200)
    comarca = models.CharField(max_length=200)
    uf = models.CharField(max_length=2)
    
