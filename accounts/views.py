from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm
from .forms import CustomAuthenticationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    
class SignUpViewSpecialist(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('/')