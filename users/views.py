from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after signup
            login(request, user)
            return redirect('car_list')  # Redirect to car list page
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Log the user in
            login(request, user)
            return redirect('car_list')  # Redirect to car list page
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


# Dashboard View (Optional, for showcasing user's dashboard if needed)
@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html', {'user': request.user})
