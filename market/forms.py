from django import forms
from .models import Aviation

class AviationForm(forms.ModelForm):
    class Meta:
        model = Aviation
        fields = '__all__'  # или перечисли нужные поля вручную
