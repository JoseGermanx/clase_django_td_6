
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'edad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': "nombre"}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'})
        }

    # validación de la edad (registro para mayores de 18 años)   
    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad < 18:
            raise forms.ValidationError("Edad debe ser mayor a 18 años")
        return edad
    
    #validación de admin en texto de input nombre

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')

        if nombre.lower() == 'admin':
            raise forms.ValidationError("No se permite el nombre 'admin'.")      
        return nombre
