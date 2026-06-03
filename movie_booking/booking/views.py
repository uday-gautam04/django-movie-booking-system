from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Movie, Show, Booking


# HOME + BOOKING
@login_required
def home(request):
    movies = Movie.objects.all()
    shows = Show.objects.all()

    if request.method == "POST":
        movie_id = request.POST.get('movie_id')
        show_id = request.POST.get('show_id')
        seats = request.POST.get('seats')

        movie = Movie.objects.get(id=movie_id)
        show = Show.objects.get(id=show_id)

        Booking.objects.create(
            movie=movie,
            show=show,
            user=request.user,
            name=request.user.username,
            seats=seats
        )

        return render(request, 'success.html')

    return render(request, 'home.html', {
        'movies': movies,
        'shows': shows
    })


# SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# ✅ NEW: MY BOOKINGS VIEW
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})