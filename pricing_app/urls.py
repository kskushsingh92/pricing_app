from django.urls import path
from . import views

urlpatterns = [
    path('', views.pricing_configuration_list, name='pricing_configuration_list'),
    path('add-pricing-configuration/', views.add_pricing_configuration, name='add_pricing_configuration'),
    path('api/calculate-price/', views.calculate_price, name='calculate_price'),
    # Add other URL patterns as needed
]