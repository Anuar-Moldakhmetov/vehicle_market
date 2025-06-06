"""
URL configuration for vehicle_market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# vehicle_market/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from market import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('market.urls')),  # Все маршруты проекта через market.urls
    path('aviation/add/', views.aviation_create, name='add_aviation'), 
    path('armored/add/', views.armored_create, name='add_armored'), 
    path('aviation/', include('aviation.urls')), 
    path('armored/', include('armored.urls')),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
