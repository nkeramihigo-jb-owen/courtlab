from django.shortcuts import render


def court_home(request):
    return render(request, 'court/court.html')