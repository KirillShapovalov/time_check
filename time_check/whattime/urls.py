from django.urls import path
from . import views


urlpatterns = [
    path('timecheck/', views.TimeCheck.as_view()),
    # path('timecheck/?checktime=<int>', views.TimeCheck.as_view())
]
