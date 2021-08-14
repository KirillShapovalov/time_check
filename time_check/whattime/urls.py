from django.urls import path
from . import views


urlpatterns = [
    path('timecheck/', views.TimeCheck.as_view()),
]
