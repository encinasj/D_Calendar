#Django
from django.urls import path

#ours
from . import views

urlpatterns = [
        path('', views.CalendarView.as_view(), name='calendar'),
        path('new/', views.event, name='new_event'),
        path('edit/', views.event, name='edit_event'),
    ]
