import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from specialties.models import Specialty






# #@login_required(login_url='login')
# def home(request):
#     queryset = get_especialties()
#     specialties = list(queryset.values())
#     #print(specialties)

#     context  = {
#         'specialties':specialties,
#         'states': BRAZILIAN_STATES,
        
#         #get_especialties()
#     }
#     print(context)
#     return render(request, 'doctor_list.html',context)


# def get_especialties():
#     specialties = Specialty.objects.all() 

#     return specialties
    
#     # return dict(
#     #     specialties = specialties,
#     # )
