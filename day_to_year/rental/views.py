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
    rental.images = request.FILES['images']
    rental.product = request.POST['product']
    rental.writer = request.POST['writer']
    rental.price = request.POST['price']
    rental.location_city = request.POST['city']
    rental.location_detail = request.POST['address']
    rental.rentterm = request.POST['rentterm']
    rental.information = request.POST['information']
    rental.save()
    return redirect('product',rental.id)
    
def edit(request, rental_id):
    edit_rental = Rental.objects.get(id= rental_id)
    return render(request,'edit.html',{'rental':edit_rental})

def update(request, rental_id):
    update_rental = Rental.objects.get(id = rental_id)
    update_rental.product = request.POST['product']
    update_rental.images = request.POST['images']
    update_rental.writer = request.POST['writer']
    update_rental.price = request.POST['price']
    update_rental.location_city = request.POST['city']
    update_rental.location_detail = request.POST['address']
    update_rental.rentterm = request.POST['rentterm']
    update_rental.information = request.POST['information']
    update_rental.save()
    return redirect('product',update_rental.id)

def delete(request, rental_id):
    delete_rental = Rental.objects.get(id = rental_id)
    delete_rental.delete()
    return redirect('rentallist')