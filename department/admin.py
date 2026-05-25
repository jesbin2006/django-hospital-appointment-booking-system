from django.contrib import admin
from home.models import Appointment
from . models import Department


admin.site.register(Appointment)
admin.site.register(Department)