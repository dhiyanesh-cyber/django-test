from django.http import JsonResponse
from .models import Doctor

def get_doctor_list(request):
    doctors = Doctor.objects.all()
    print(doctors)
    doctor_list = [{"id": doctor.id, "name": doctor.name, "age": doctor.age, "discipline": doctor.discipline} for doctor in doctors]
    return JsonResponse({"doctors": doctor_list})
