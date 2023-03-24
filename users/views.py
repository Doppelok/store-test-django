from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from django.contrib.auth.models import User


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login_form.html'
    authentication_form = UserLogInForm


class RegistrationView(CreateView):
    model = User
    template_name = 'users/register_form.html'
    form_class = NewUserForm
    success_url = reverse_lazy('users:login')


class UserLogOutView(LogoutView):
    pass
