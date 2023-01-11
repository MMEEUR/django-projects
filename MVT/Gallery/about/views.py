from django.shortcuts import render
from account.models import Profile

# Create your views here.
def aboutView(request):
    users = Profile.objects.all()
    
    return render(request, 'about/about_us.html', {'users': users})