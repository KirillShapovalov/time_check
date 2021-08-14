from django.urls import path
from .views import time_check
from . import views

urlpatterns = [
    path('timecheck/', views.time_check, name='time-check'),
]
