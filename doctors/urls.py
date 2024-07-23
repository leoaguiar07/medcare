from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('doctors/list/', views.DoctorListView.as_view(), name='doctor_list'),
    # path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctors/<int:pk>/detail/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('dados/', TemplateView.as_view(template_name='dados.html'), name='dados'),
    # path('doctors/<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    # path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor_delete'),

    # path('api/v1/doctors/', views.DoctorCreateListAPIView.as_view(), name='doctor-create-list-api-view'),
    # path('api/v1/doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail-api-view'),
    
    # API
    path('api/v1/doctors/', views.DoctorCreateListAPIView.as_view(), name='doctor-create-list-api-view'),
    path('api/v1/doctors/<int:pk>/', views.DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-detail-api-view'),
]
