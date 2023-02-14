from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            full_message = "{} with \"{}\" number:\t{}".format(name, phone, message)
            
            try:
                send_mail(subject, full_message, email, ['a@gmail.com'], fail_silently=False)
            
            except BadHeaderError:
                raise form.add_error('Oops! form Does not send')
        
            return redirect(request.path)
        
    else:
        form = ContactForm()
        
    context = {
        'form': form
    }
        
    return render(request, 'contact/contact.html', context=context)
