from datetime import datetime
from django.shortcuts import render
from .models import Oferta
from django.http import Http404 

# Create your views here.

def index(request):
    current_date = datetime.now()
    ofertas=[]

    try:
        ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date, 
        fecha_fin__gte=current_date)
        raise Exception("no hay ofertas disponibles en este momento")
        if not ofertas:
            raise ValueError("no hay ofertas disponibles en este momento")
    except ValueError as e:
        #manejo de error especifico  
        return render(request, 'ofertas/index.html', {'error': str(e), 
        'current_date': current_date})
    except Exception as e:
        #Manejo de cualquier otro error       
        return render(request, 'ofertas/index.html', 
        {'error': 'Se produjo  un errror inesperado!', 'current_date': current_date})
    context={
        'current_date': current_date,
        #is_special_offer: False #false para no y true para si
        'ofertas': ofertas
    }
    return render(request, 'ofertas/index.html', context)