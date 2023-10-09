from django.urls import path, include

urlpatterns = [
    path('', include('pricing_app.urls')),
    # Add other URL patterns as needed
]