from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Parientes

def home(request):
    return HttpResponse('Listado Familiar')

def homePage(self):
    data = {'nombre':'Marta','apellido':'Sosa'}
    planilla = loader.get_template('index.html')
    documento = planilla.render(data)
    return HttpResponse(documento)


def Familiares(self):
    listadefamiliares = []
    
    Familiares1 = Parientes(id='1',nombreyapellido='Maria Andrea Sosa', fechanacimiento='1952-08-09',edad = '68')
    Familiares1.save()
    Familiares2 = Parientes(id='2',nombreyapellido='Estefania Tolisano', fechanacimiento='1987-02-01',edad = '35')
    Familiares2.save()
    Familiares3 = Parientes(id='3',nombreyapellido='Alfredo Andres Tolisano', fechanacimiento='1948-09-06',edad = '74')
    Familiares3.save()

    listadefamiliares.append(Familiares1)
    listadefamiliares.append(Familiares2)
    listadefamiliares.append(Familiares3)

    data = {'listadefamiliares': listadefamiliares}
    planilla = loader.get_template('familiares.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

