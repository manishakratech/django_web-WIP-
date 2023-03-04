from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Driver, CustomerOrder

def home(request):
    return render(request, "driver/home.html")

def driver_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        driver = authenticate(request, driver_email=email, driver_password=password)

        if driver is not None:
            request.session['driver_id'] = driver.driver_id

            return redirect(reverse('driver-detail', kwargs={'driver_id': driver.driver_id}))
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 'driver/driver_login.html', {'error_message': error_message})

    return render(request, 'driver/driver_login.html')

def driver_id(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        driver = authenticate(request, driver_email=email, driver_password=password)

        if driver is not None:
            request.session['driver_id'] = driver.driver_id
            return redirect(reverse('driver-detail', kwargs={'driver_id': driver.driver_id}))
        else:
            error_message = "Invalid email or password. Please try again."
            return render(request, 'driver/driver_login.html', {'error_message': error_message})

    return render(request, 'driver/driver_login.html')

def driver_detail(request, driver_id):
    if 'driver_id' not in request.session:
        return redirect('driver-login') 
    else:
        if request.method == 'POST':
            store = request.POST.get('store')
            vehicle = request.POST.get('vehicle')
            shift = request.POST.get('shift')
            date = request.POST.get('date')

            order = get_object_or_404(CustomerOrder, store=store, date=date, vehicle=vehicle, shift=shift)
            waypoints = order.waypoints
            summary = order.summary

            context = {'store':store, 'vehicle':vehicle, 'shift':shift, 'date':date, 'waypoints':waypoints, 'summary':summary}
            return render(request, 'driver/delivery.html',context)

        return render(request, 'driver/delivery_home.html')