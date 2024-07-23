from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, SignUpViewSpecialist, CustomLogoutView

from .views import CustomLoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup_specialist/', SignUpViewSpecialist.as_view(), name='signup_specialist'),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]