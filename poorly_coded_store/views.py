from django.shortcuts import render, redirect
from .models import Order, Product

def home_reroute(request):
    return redirect('/amadon')

def amadon(request):
    return render(request, "index.html")