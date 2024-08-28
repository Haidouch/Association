from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service/SoutienPsychologique', views.service1, name='service1'),
    path('service/PlansDeTraitement', views.service2, name='service2'),
    path('service/ConsultationPourLesMaladiesRénales', views.service3, name='service3'),
    path('service/ConseilsNutritionnels', views.service4, name='service4'),
    #path('dataplot', views.data_plot_view, name='dataplot'),
]