from django.shortcuts import render, get_object_or_404,redirect
from .models import Car
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Car
from django.shortcuts import render
from django.db.models import Q
from .models import Car

def car_list(request):
    query = request.GET.get('q', '')
    cars = Car.objects.filter(user=request.user)  # Filter cars for the logged-in user

    # Apply search functionality
    if query:
        cars = cars.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        )

    # Pagination
    paginator = Paginator(cars, 6)  # Show 6 cars per page
    page_number = request.GET.get('page')
    cars_page = paginator.get_page(page_number)

    return render(request, 'cars/car_list.html', {
        'cars': cars_page,
        'query': query,
        'is_paginated': cars_page.has_other_pages(),
    })



def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk, user=request.user)
    return render(request, 'cars/car_detail.html', {'car': car})

from django.http import HttpResponseRedirect
from .forms import CarForm

def car_create_update(request, pk=None):
    # Check if updating an existing car
    if pk:
        car = get_object_or_404(Car, pk=pk, user=request.user)
    else:
        car = None

    # Handle form submission
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)  # Ensure request.FILES for image upload
        if form.is_valid():
            new_car = form.save(commit=False)
            new_car.user = request.user  # Assign the user
            new_car.save()
            return redirect('car_list')  # Redirect to the car list page
    else:
        form = CarForm(instance=car)

    # Render the car form template
    return render(request, 'cars/car_form.html', {'form': form, 'heading': 'Add New Car' if not pk else 'Edit Car'})

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk, user=request.user)
    car.delete()
    return redirect('car_list')
