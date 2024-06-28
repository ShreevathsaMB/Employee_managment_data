from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'doj': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
