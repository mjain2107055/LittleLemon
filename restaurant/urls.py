from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingView.as_view()),
    path('bookings/<int:pk>', views.SingleBookingView.as_view()),
   
]