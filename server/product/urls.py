from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addProduct, name='add-product'),
    path('edit/<int:pk>', views.editProduct, name='edit-product'),
    path('view/<int:pk>', views.viewProduct, name='view-product'),
    path('delete/<int:pk>', views.deleteProduct, name='delete-product'),
    path('review/<int:pk>', views.review, name='review')
]