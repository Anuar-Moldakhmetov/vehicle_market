from django import forms
from .models import Aviation
from .models import ArmoredVehicles


class AviationForm(forms.ModelForm):
    class Meta:
        model = Aviation
        fields = '__all__'  # или перечисли нужные поля вручную

class ArmoredVehiclesForm(forms.ModelForm):
    class Meta:
        model = ArmoredVehicles
        fields = '__all__'