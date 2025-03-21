from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from .models import EmployeeModel


class DeleteModal(View):
    def get_employee(self, id):
        return get_object_or_404(EmployeeModel, id=id)
    
    def render_page(self, request, employee):
        context = {'employee': employee}
        return render(request, 'partials/sections/modal/form_delete.html', context=context)
    
    def get(self, request, id):
        employee = self.get_employee(id=id)
        return self.render_page(request, employee)
    
    def post(self, request, id):
        employee = self.get_employee(id)
        employee.delete()
        messages.success(request, 'Funcionario Removido com sucesso!')
        
        return redirect(reverse('index'))