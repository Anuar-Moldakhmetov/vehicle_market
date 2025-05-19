from django.shortcuts import render
from .models import Aviation, ArmoredVehicles
from .forms import AviationForm
    
def home(request):
    return render(request, 'market/home.html')

def aviation_list(request):
    aviation = Aviation.objects.all()
    return render(request, 'market/aviation_list.html', {'aviation': aviation})

def aviation_create(request):
    if request.method == 'POST':
        form = AviationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aviation_list')
    else:
        form = AviationForm()
    return render(request, 'market/aviation_create.html', {'form': form})
      

def armored_list(request):
    armored = ArmoredVehicles.objects.all()
    return render(request, 'market/armored_list.html', {'armored': armored})

