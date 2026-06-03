from django.contrib import admin
from django.urls import path
from booking.views import home, signup_view, login_view, logout_view, my_bookings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('my-bookings/', my_bookings, name='my_bookings'),
]