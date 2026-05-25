from django.urls import path,include
from . import views



urlpatterns = [

    
    
    path('', views.index,name='home'),
    path('register/', views.login_user,name='register'),
    path('logout',views.user_logout,name='logout'),
    path('user_login',views.otp,name='go_login_otp')
    
]