from django.views.generic import ListView, DetailView
from rest_framework import generics
from . import models, serializers 

from specialties.models import Specialty
from django.db.models import Avg
from app.utils import maps
from django.utils import timezone
from datetime import timedelta





class DoctorListView(ListView):
    model = models.Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'
    paginate_by = 10
    #permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        specialties = self.request.GET.get('specialties')     

        if name:
            queryset = queryset.filter(name__icontains=name)
                
        if city:
             queryset = queryset.filter(address__city__icontains=city)
            
        if specialties:
             queryset = queryset.filter(specialty__name__icontains=specialties)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        doctors = context['doctors']
        # context['statestate'] = models.Address.objects.values_list('state', flat=True).distinct()
        
        # Adicionando a contagem de avaliações para cada médico
        for doctor in doctors:
            evaluations = doctor.evaluations.all()
            doctor.evaluation_count = doctor.evaluations.count()
            doctor.average_result = evaluations.aggregate(Avg('result'))['result__avg'] or 0

            # Adicionar uma lista de estrelas para cada médico
            stars_filled = int(doctor.average_result)
            stars_unfilled = 5 - stars_filled
            doctor.stars = ['filled'] * stars_filled + ['unfilled'] * stars_unfilled

        context['specialties'] = Specialty.objects.all()
        context['states'] = models.Address.objects.all()
        context['addresses'] = models.Address.objects.all()
        context['doctors_count'] = models.Doctor.objects.count()
       
        return context
    

class DoctorDetailView(DetailView):
    model = models.Doctor
    template_name = 'doctor_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        today = timezone.now().date()
        
        context['addresses'] = self.object.address.all()  # Usando o related_name 'addresses'


  # Encontrar o início e fim da semana atual (considerando que a semana começa na segunda-feira)
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        # Filtrar os objetos Schedule para a semana atual
        weekly_schedule = models.Schedule.objects.filter(datetime__date__range=[start_of_week, end_of_week])

        # Criar um dicionário para armazenar os eventos por dia
        days_of_week = {}
        for i in range(7):
            current_day = start_of_week + timedelta(days=i)
            days_of_week[current_day] = weekly_schedule.filter(datetime__date=current_day)

        context['days_of_week'] = days_of_week
        context['start_of_week'] = start_of_week
        context['end_of_week'] = end_of_week


        return context
    



# API 

class DoctorCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer


class DoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
