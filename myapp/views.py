from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking




def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def services(request):
    return render(request, 'myapp/services.html')

def gallery(request):
    return render(request, 'myapp/gallery.html')

def team(request):
    return render(request, 'myapp/team.html')

@login_required(login_url='login')
def booking(request):
    if request.method == 'POST':
        service = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')
        notes = request.POST.get('notes')
        
        if service and date and time:
            booking = Booking.objects.create(
                user=request.user,
                service=service,
                date=date,
                time=time,
                notes=notes
            )
            messages.success(request, "Your luxury ritual has been reserved. Check your profile for details!")
            return redirect('profile')
        else:
            messages.error(request, "Please fill in all required fields.")
            
    return render(request, 'myapp/booking.html')

def sentmessage(request):
    return render(request, 'myapp/sentmessage.html')

def request_view(request):
    return render(request, 'myapp/request.html')

@login_required(login_url='login')
def profile(request):
    # Fetch user's bookings
    user_bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, 'myapp/profile.html', {'bookings': user_bookings})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('booking')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Registration successful. Welcome to The Better Feel!")
            return redirect('home')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')




from django.shortcuts import render, redirect
from django.contrib import messages   # 👈 add this
from .forms import ContactForm

@login_required(login_url='/login/') 
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "✨ Your message has been submitted successfully!")  # ✅

            return redirect('myapp/contact.html')

        else:
            messages.error(request, "❌ Something went wrong. Please try again.")

    else:
        form = ContactForm()

    return render(request, 'myapp/contact.html', {'form': form})
