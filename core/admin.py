from django.contrib import admin
from .models import EmployeeModel
# Register your models here.


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'adress', 'phone']
    ordering = ['-id']