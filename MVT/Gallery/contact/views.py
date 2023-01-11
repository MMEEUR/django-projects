from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name =  form.cleaned_data["name"]
            subject = form.cleaned_data["subject"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data['message']
            
            try:
                send_mail(subject, message, email, ["admin@example.com"])
            except BadHeaderError:
                raise form.add_error('فرم ارسال نمیشود!')
            
            return redirect("contact:contact_done")
    
    else:
        form = ContactForm()
        
    return render(request, "contact/contact.html", {"form": form})

def contactDoneView(request):
    
    return render(request, "contact/contact_done.html")