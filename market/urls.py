from django.urls import path
import market.views as views

urlpatterns = [
    path('', views.home),
    path('aviation', views.aviation_list),
    path('armored', views.armored_list),
]