
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib import messages
from .models import EmployeeModel
from .forms import EmployeeForm

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