from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, LoginForm2, RegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile 

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('با موفقیت وارد شدید')
                else:
                    return HttpResponse('این حساب کار غیر فعال است')
            else:
                return HttpResponse('نام کاربری یا رمز عبور اشتباه است')
    else:
        form = LoginForm()
        
    return render(request, 'account/register_login.html', {'form': form})

def user_register(request):
    if request.user.is_authenticated:
        
        return redirect('account:dashboard')
    
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
        
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
        
    return render(request, 'account/register.html', {'user_form': user_form})
    
class UpdatedLoginView(LoginView):
    form_class = LoginForm2
    
    def form_valid(self, form):
       
        remember_me = form.cleaned_data['remember_me']  # get remember me data from cleaned_data of form
        if not remember_me:
            self.request.session.set_expiry(0)  # if remember me is 
            self.request.session.modified = True
        return super(UpdatedLoginView, self).form_valid(form)    

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'ویرایش پروفایل با موفقیت انجام شد')
        
        else:
            messages.error(request, 'خطایی رخ داداه است')
                
            
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})