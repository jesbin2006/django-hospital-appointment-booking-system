from django.shortcuts import render
from . models import Doctors
# Create your views here.
def list_doctors(request):
    doctor=Doctors.objects.all()
    context={
        'doctor':doctor
    }
    return render(request,'doctors.html',context)

def about_doctors(request,pk):
    doc=Doctors.objects.get(pk=pk)
    context={
        'doc':doc
    }
    return render (request,'doctors_list.html',context)