import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Desafio_urbano.settings")
django.setup()

import csv
from processoApp.models import Processo

with open('processos.csv', 'r') as csv_file :

    ler = csv.reader(csv_file, delimiter =';')
    next(ler)
    for colunas in ler:
        Processo.objects.all()
        pasta = colunas[0]
        comarca = colunas[1]
        uf = colunas[2]
        coluna = Processo(
                          pasta = pasta,
                          comarca = comarca,
                          uf = uf,
                          )
        coluna.save()
        print (coluna.pasta+" "+coluna.comarca +" "+coluna.uf)
        
        
        
