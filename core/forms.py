from django import forms
from django.core.exceptions import ValidationError

from .models import EmployeeModel

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'email', 'adress', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            'adress': forms.Textarea(attrs={'required': 'True'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
        }

    def clean_email(self):
        data_email = self.cleaned_data.get('email')
        exist = EmployeeModel.objects.filter(email=data_email).exists()
        
        if exist:
            raise ValidationError(
                'Este email ja foi cadastrado!'
            )
        return data_email
            
    def clean_phone(self):
        data_phone = self.cleaned_data.get('phone')
        exist = EmployeeModel.objects.filter(phone=data_phone).exists()
        
        if exist:
            raise ValidationError(
                'Este Telefone ja foi cadastrado!'
            )
        return data_phone
    
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['name', 'email', 'adress', 'phone']