from django.urls import path,include
from . import views



urlpatterns = [

    path('appointment/',views.appointment,name='appointment'),
    path('department/',views.department,name='department'),
    path('list_doctors/<int:pk>',views.list_doctors,name='see_doctors'),
    path('my-appointments/',views.my_appointments,name='my_appointments'),
    path('edit-appointment/<int:pk>/',views.edit_appointment,name='edit_appointment'),
    path('delete-appointment/<int:pk>/',views.delete_appointment,name='delete_appointment'),
    path('load-doctors/', views.load_doctors, name='load_doctors'),
   
]