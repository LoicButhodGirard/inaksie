from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('porfolio/', views.portfolio, name='porfolio'),
    path('contact/', views.contact, name='contact'),
    path('werkwijze/', views.werkwijze, name='werkwijze'),
    path('intro/', views.intro, name='intro'),
]
