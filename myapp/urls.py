# myapp/urls.py
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('api/doctors/', views.doctor_list.as_view(), name='doctor_list'),
    # path('api/doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('add-doctor/', views.add_doctor, name='add_doctor'),
    path('doctor-list/', views.doctor_list, name='doctor_list'),
]

