from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tables',views.BookingViewSet, basename='booking')

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls)),
]