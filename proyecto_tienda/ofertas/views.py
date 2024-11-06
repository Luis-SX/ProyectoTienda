from datetime import datetime
from django.shortcuts import render
from .models import Oferta

# Create your views here.
current_date = datetime.now()
ofertas = Oferta.objects.filter(fecha_inicio__lte=current_date, 
fecha_fin__gte=current_date)

def index(request):
    context={
        'current_date': current_date,
        #is_special_offer: False #false para no y true para si
        'ofertas': ofertas
    }
    return render(request, 'ofertas/index.html', context)