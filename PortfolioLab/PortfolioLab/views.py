from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def add_donation(request):
    return render(request, 'add_donation.html')

def register_view(request):
    return render(request, 'register.html')