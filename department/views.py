from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import AppointmentForm
from .models import Department
from doctors.models import Doctors
from home.models import Appointment


def department(request):
    departlevel = Department.objects.all()

    return render(request, 'department.html', {
        'departlevel': departlevel
    })


def appointment(request):

    departlevel = Department.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('my_appointments')

        else:
            print(form.errors)

    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {
        'form': form,
        'departlevel': departlevel
    })


# AJAX
def load_doctors(request):

    department_id = request.GET.get('department_id')

    if not department_id:
        return JsonResponse({'doctors': []})

    doctors = Doctors.objects.filter(
        department_id=department_id,
        active=True
    )

    data = list(doctors.values('id', 'name'))

    return JsonResponse({'doctors': data})


def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)

    return render(request, 'my_appointments.html', {
        'appointments': appointments
    })

def edit_appointment(request, pk):

    appointment = get_object_or_404(Appointment, id=pk, user=request.user)

    departlevel = Department.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()
            return redirect('my_appointments')

        else:
            print(form.errors)

    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'appointment.html', {
        'form': form,
        'departlevel': departlevel,
        'edit_mode': True
    })

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, id=pk, user=request.user)

    if appointment.status == 'confirmed':
        return redirect('my_appointments')

    appointment.delete()
    return redirect('my_appointments')


def list_doctors(request, pk):
    doctor = Doctors.objects.filter(department_id=pk)

    return render(request, 'list.html', {
        'doctor': doctor
    })

