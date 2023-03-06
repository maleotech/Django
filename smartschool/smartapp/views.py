from django.shortcuts import render
from .models import Activity, Alumni

def LandingPageView(request):
    activities = Activity.objects.all()
    alumni = Alumni.objects.filter(is_display = True).order_by("-created_date")[:5]
    return render(request, 'home.html', {'activities': activities, 'alumni': alumni})


