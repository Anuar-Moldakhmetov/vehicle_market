from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'market/aviation_list.html')

