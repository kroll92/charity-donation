
from .models import Bag, Institution
from django.shortcuts import render
from django.db import models

def landing_page(request):
    return render(request, 'landing.html')

def add_donation(request):
    return render(request, 'add_donation.html')

def register_view(request):
    return render(request, 'register.html')


def index(request):
    total_bags = Bag.objects.aggregate(total_quantity=models.Sum('quantity'))['total_quantity'] or 0
    supported_institutions = Institution.objects.count()

    context = {
        'total_bags': total_bags,
        'supported_institutions': supported_institutions,
    }

    return render(request, 'index.html', context)