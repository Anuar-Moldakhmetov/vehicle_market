#from django.urls import path
#import market.views as views
#from django.conf import settings
#from django.conf.urls.static import static
# market/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Корень сайта
    path('aviation/', views.aviation_list, name='aviation_list'),
    path('aviation/add/', views.aviation_create, name='aviation_create'),
    path('armored/', views.armored_list, name='armored_list'),  
    path('armored/add/', views.armored_create, name='armored_create'),
]

