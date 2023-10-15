from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'), 
    path('api/menu-items/', views.MenuItemView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/', views.BookingView.as_view()),
    path('api/bookings/<int:pk>', views.SingleBookingView.as_view()),
   
]