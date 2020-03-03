from django.urls import path
from . import views

urlpatterns = [
    path('add-to-cart/<int:pk>', views.add_to_cart, name='add-to-cart'),
    path('view-cart', views.view_cart, name='view-cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart, name='remove-from-cart'),
]