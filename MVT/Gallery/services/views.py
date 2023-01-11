from django.shortcuts import render

# Create your views here.
def servicesView(request):
    
    return render(request, 'services/services.html')