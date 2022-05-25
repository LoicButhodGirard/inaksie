from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('werkwijze/', views.werkwijze, name='werkwijze'),
    path('intro/', views.intro, name='intro'),
]
