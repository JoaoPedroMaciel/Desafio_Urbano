import csv
import io
from processoApp.models import Processo
from django.http import HttpResponse
from django.shortcuts import render

def index(request):  
    return HttpResponse("Cadastro de processo index.")

def save_data(data):

    aux = []
    for item in data:
        pasta = item.get('pasta')
        comarca = item.get('comarca')
        uf = item.get('uf')
        obj = Processo(
            pasta = pasta,
            comarca = comarca,
            uf = uf,
        )
        aux.append(obj)
    Processo.objects.bulk_create(aux)
    save_data(data)

def import_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('processo:processo_list'))

    template_name = 'processo_import.html'
    return render(request, template_name)
