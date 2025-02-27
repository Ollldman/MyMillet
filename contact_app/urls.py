from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('success/', views.success_feedback, name='success_feedback')
]
