from django.urls import path

#ours
from . import views

app_name='Dcalendar'
urlpatterns = [
        path('', views.CalendarView.as_view(), name='calendar'),
    ]
