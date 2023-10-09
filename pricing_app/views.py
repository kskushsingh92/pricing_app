from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import PricingConfiguration
from .forms import PricingConfigurationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response

def pricing_configuration_list(request):
    configurations = PricingConfiguration.objects.all()
    return render(request, 'configuration_list.html', {'configurations': configurations})

def add_pricing_configuration(request):
    if request.method == 'POST':
        form = PricingConfigurationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pricing_configuration_list')
    else:
        form = PricingConfigurationForm()
    return render(request, 'add_configuration.html', {'form': form})

@api_view(['POST'])
def calculate_price(request):
    distance = float(request.data.get('distance', 0))
    time = float(request.data.get('time', 0))
    day_of_week = request.data.get('day_of_week', 'Mon')  # You should validate this input

    # Retrieve the applicable pricing configuration based on the day of the week
    configuration = PricingConfiguration.objects.filter(day_of_week=day_of_week, is_enabled=True).first()

    if configuration:
        dbp = configuration.distance_base_price
        dap = configuration.distance_additional_price
        tmf = configuration.time_multiplier_factor
        wc = configuration.waiting_charges

        price = (dbp + (distance * dap)) + (time * tmf) + wc

        return Response({'price': price})
    else:
        return Response({'error': 'No pricing configuration found for this day of the week.'})


