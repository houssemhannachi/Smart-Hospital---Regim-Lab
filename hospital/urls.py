from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('doctor_login', views.doctor_login),
    path('doctor_register', views.doctor_register),
    path('patient_login', views.patient_login),
    path('patient_register', views.patient_register),
    path('nurse_login', views.nurse_login),
    path('nurse_register', views.nurse_register),
    path('receptionist_login', views.receptionist_login),
    path('receptionist_register', views.receptionist_register),
    path('patient_add', views.patient_add),
    path('logout', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]