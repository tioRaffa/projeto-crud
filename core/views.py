from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View, DeleteView, CreateView, UpdateView
from .models import EmployeeModel
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy

class IndexView(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all()
    template_name = 'pages/index.html'
    context_object_name = 'employees'
    
    
class DeleteModal(View):
    def get_employee(self, request, id):
        return get_object_or_404(EmployeeModel, id=id)
    
    def redirect_page(self):
        return redirect('index')
    
    def post(self, request, id):
        employee = self.get_employee(request, id)
        employee.delete()
        # messages.success(request, 'Receita Apagada com Sucesso')
        
        return self.redirect_page()
