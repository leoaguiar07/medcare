
from django.contrib import admin
from django.urls import path, include
from . import views
from doctors.views import DoctorListView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('', include('doctors.urls')),
    # path('contact/', TemplateView.as_view(template_name='contato.html'), name='contato'),
    path('contact/', include('contact.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),  # Inclui as URLs padrão de autenticação
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

