from django import forms

class login(forms.Form):
    # Define los campos de tu formulario aquí
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    # Otros campos y validaciones si es necesario
