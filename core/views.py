from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View, DeleteView, CreateView, UpdateView
from .models import EmployeeModel
from .forms import EmployeeForm
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.contrib import messages
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
        messages.success(request, 'Funcionario removido com Sucesso')
        
        return self.redirect_page()
    

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
    

    
class UpdateViewEmployee(View):
    def get_employee(self, id=None):
        if id is not None:
            return get_object_or_404(EmployeeModel, id=id)
        
    def render_page(self, employee, form):
        context = {
            'employee': employee,
            'form': form
        }
        
        return render(self.request, 'partials/sections/modal/edit_modal.html')
    
    def get(self, request, id):
        employee = self.get_employee(id=id)
        form = EmployeeForm(instance=employee)
        
        return self.render_page(employee, form)
    
    def post(self, request, id):
        employee = self.get_employee(id)
        form = EmployeeForm(data=request.POST, instance=employee)
        
        if form.is_valid():
            form.save()
            
            form = EmployeeForm()
            messages.success(request, 'Funcionario atualizado com Sucesso')
            
            return redirect(reverse('index'))

        else:
            print(form.errors)
            messages.error(request, 'Erro! Tente Novamente.')
            return redirect(reverse('index'))

        return self.render_page(employee, form)