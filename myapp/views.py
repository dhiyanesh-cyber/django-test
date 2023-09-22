# views.py
from django.shortcuts import render, redirect
from .forms import DoctorForm
from .models import Doctor  # Import the Doctor model


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the doctor list page
    else:
        form = DoctorForm()
    return render(request, 'add_doctor.html', {'form': form})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})