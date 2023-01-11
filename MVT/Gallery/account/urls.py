from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import EmailValidationOnForgotPassword
from .views import UpdatedLoginView, dashboard, user_register, edit_profile

app_name = 'account'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register', user_register, name='register'),
    path('edit', edit_profile, name='edit'),
    path('login', UpdatedLoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword, success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #path('register_login/', views.user_login, name='register_login')password_reset/done
]
