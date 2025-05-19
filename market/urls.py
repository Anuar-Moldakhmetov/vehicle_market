#from django.urls import path
#import market.views as views
#from django.conf import settings
#from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Добавим простую заглушку
from django.conf import settings
from django.conf.urls.static import static
import market.views as views

def home(request):
    return HttpResponse("Добро пожаловать на Vehicle Market!")

urlpatterns = [
    path('', home),  # Корень сайта
    path('admin/', admin.site.urls),
    path('aviation/', include('aviation.urls')),
    path('armored/', include('armored.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('', views.home),
    path('aviation', views.aviation_list),
    path('armored', views.armored_list),
]

