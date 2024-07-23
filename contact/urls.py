# urls.py
from django.urls import path
from .views import contato, contato_sucesso

urlpatterns = [
    path('contato/', contato, name='contato'),
    path('contato/sucesso/', contato_sucesso, name='contato_sucesso'),
]
