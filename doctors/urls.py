from django.urls import path,include
from . import views



urlpatterns = [

    path('doctors/',views.list_doctors,name='doctors'),
    path('about_doctors/<int:pk>',views.about_doctors,name='see')
   
]