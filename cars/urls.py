from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),  # Matches redirect('car_list')
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('<int:pk>/edit/', views.car_create_update, name='car_edit'),
    path('new/', views.car_create_update, name='car_new'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
]
