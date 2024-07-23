from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

    
    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['password1'].help_text = ''
    #    self.fields['password2'].help_text = ''


    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2')
    #     widgets = {
    #         'username': forms.TextInput(attrs={
    #             'placeholder': 'Usuário',
    #             'class': 'mb-20px bg-very-light-gray form-control',
    #             }),
    #         'password1': forms.PasswordInput(attrs={
    #             'placeholder': 'Password',
    #             'class': 'mb-20px bg-very-light-gray form-control',
    #             }),
    #         'password2': forms.PasswordInput(attrs={
    #             'placeholder': 'Confirm Password',
    #             'class': 'mb-20px bg-very-light-gray form-control',
    #             }),
    #     }
    #     help_texts = {
    #         'username': None,
    #     }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Usuário', 
            'class': 'mb-20px bg-very-light-gray form-control',
           
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Senha', 
            'class': 'mb-20px bg-very-light-gray form-control',
            
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirme a senha', 
            'class': 'mb-20px bg-very-light-gray form-control',
            
        })
        # Remova os help_texts manualmente
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

   
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Usuário',
            'class': 'mb-20px bg-very-light-gray form-control',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Senha',
            'class': 'mb-20px bg-very-light-gray form-control',
        })
    )