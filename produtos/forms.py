from django import forms
from produtos.models import Usuario

class DatePickerInput(forms.DateInput):
        input_type = 'date'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= '__all__'  
    
        widgets = {
            'data_nascimento': forms.TimeInput(attrs={'type': 'date'}),
            'cpf': forms.TextInput(attrs={'data-mask': '000.000.000-00'})
        }