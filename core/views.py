from django.shortcuts import render
from django.views.generic import ListView
from .models import EmployeeModel
from django.shortcuts import render, get_object_or_404, get_list_or_404

class IndexView(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all()
    template_name = 'pages/index.html'
    context_object_name = 'employees'
    