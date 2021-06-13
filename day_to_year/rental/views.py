from django.shortcuts import render, redirect
from .models import Rental

def rental(request):
    rentals = Rental.objects.all()
    return render(request, "rental.html",{'rentals':rentals})

def product(request, rental_id):
    rental = Rental.objects.get(id = rental_id)
    return render(request, "product.html",{'rental':rental})

def new(request):
    return render(request, "new.html")

def submit(request):
    rental = Rental()
    rental.product = request.POST['product']
    rental.writer = request.POST['writer']
    rental.price = request.POST['price']
    rental.location_city = request.POST['city']
    rental.location_detail = request.POST['address']
    rental.rentterm = request.POST['rentterm']
    rental.information = request.POST['information']
    rental.save()
    return redirect('product',rental.id)
    
