from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pasta', views.pasta, name='pasta'),
    path('flour', views.flour, name='flour'),
    path('croup', views.croup, name='croup'),
]