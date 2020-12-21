#Django
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

#ours
from .models import Event
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #use to day's date  for the calendar
        d = get_date(self.request.GET.get('month', None))

        ##instantie our calendar class with to day's year and date
        cal = Calendar(d.year, d.month)

        #call the formatmonth method, which return our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
