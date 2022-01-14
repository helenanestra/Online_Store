from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')


def cart_view(request):
    return render(request, 'cart.html')


def checkout_view(request):
    return render(request, 'checkout.html')
