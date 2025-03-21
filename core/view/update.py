from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View
from .models import EmployeeModel
from .forms import EmployeeUpdateForm
from django.contrib import messages


class UpdateView(View):
    def get_employee(self, id=None):
        if id is not None:
            return get_object_or_404(EmployeeModel, id=id)
        
    def render_page(self, employee, form):
        context = {
            'employee': employee,
            'form': form
        }
        
        return render(self.request, 'partials/sections/modal/form_edit.html', context=context)
    
    def get(self, request, id):
        employee = self.get_employee(id=id)
        form = EmployeeUpdateForm(data=request.POST or None, instance=employee)
        
        return render(request, 'partials/sections/modal/form_edit.html', {'employee': employee, 'form': form})
    
    def post(self, request, id):
        employee = self.get_employee(id)
        form = EmployeeUpdateForm(data=request.POST or None, instance=employee)
        
        if form.is_valid():
            form.save()
            form = EmployeeUpdateForm()
            messages.success(request, 'Funcionario atualizado com Sucesso')
            
            return redirect(reverse('index'))

        else:
            print(form.errors)
            messages.error(request, 'Erro! Tente Novamente.')
            return redirect(reverse('index'))

        return self.render_page(employee, form)