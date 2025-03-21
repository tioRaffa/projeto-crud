from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View, DeleteView, CreateView, UpdateView
from .models import EmployeeModel
from .forms import EmployeeForm, EmployeeUpdateForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
class IndexView(ListView):
    model = EmployeeModel
    queryset = EmployeeModel.objects.all().order_by('-id')
    template_name = 'pages/index.html'
    context_object_name = 'employees'
    
    
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

class CreateView(View):
    def render_page(self, request, form):
        context = {
            'form': form
        }
        return render(request, 'partials/sections/modal/create_modal.html', context=context)
    
    def get(self, request):
        form = EmployeeForm()
        return self.render_page(request, form)
    
    def post(self, request):
        form = EmployeeForm(data=request.POST)
        
        if form.is_valid():
            employee: EmployeeModel = form.save(commit=False)
            employee.save()    
                    
            form = EmployeeForm()
            messages.success(request, 'Funcionario adicionado com Sucesso')
            
            return redirect(reverse('index'))
        else:
            
            print(form.errors)
            messages.error(request, 'Erro! Tente Novamente.')
            return redirect(reverse('index'))
        
        return self.render_page(request, form)
    

    
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