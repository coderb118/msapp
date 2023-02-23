from django.urls import path
from . import views


urlpatterns = [
    path('', views.Robotchecker, name='robotchecker'),
    path('login/', views.EmailLogin, name='elogin'),
    path('login/p/', views.passwordlLogin, name='plogin'),
    path('login/cp/', views.cpasswordlLogin, name='cplogin'),
    
]
