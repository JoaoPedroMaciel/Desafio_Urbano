import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Desafio_urbano.settings")
django.setup()

import csv
from processoApp.models import Processo

with open('processos.csv', 'r') as csv_file :

    ler = csv.reader(csv_file, delimiter =';', fieldnames =["pasta", "comarca", "uf"])
    next(ler)
    for coluna in ler:
        Processo.objects.all()
        
        print (coluna)
        
        
        
