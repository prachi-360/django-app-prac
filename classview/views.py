from django.shortcuts import render
from django.views.generic import ListView
from .models import Hr

class HrList(ListView):
    model = Hr
    hrlist = model.objects.all()
    template_name = 'classview/hr_list.html'
    context_object_name = 'hrlist'

