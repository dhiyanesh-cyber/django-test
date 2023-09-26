from django.urls import path
from . import views

urlpatterns = [
    path('get_doctor_list/', views.get_doctor_list, name='get_doctor_list'),
]
