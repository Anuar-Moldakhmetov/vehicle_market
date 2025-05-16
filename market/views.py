from django.shortcuts import render
from .models import Aviation, ArmoredVehicles
    
def home(request):
    return render(request, 'market/home.html')

def aviation_list(request):
    aviation = Aviation.objects.all()
    return render(request, 'market/aviation_list.html', {'aviation': aviation})

def armored_list(request):
    armored = ArmoredVehicles.objects.all()
    return render(request, 'market/armored_list.html', {'armored': armored})