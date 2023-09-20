from django.shortcuts import render
from rest_framework.views import APIView
import requests

########correo############
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from .forms import login  # Asegúrate de que el formulario se llame 'login'

# Vista de registro de usuario
def registro_usuario(request):
    if request.method == 'POST':
        form = login(request.POST)  # Utiliza el formulario 'login' aquí
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente al usuario

            # Envía un correo con los datos de inicio de sesión
            enviar_correo_registro(user)

            return redirect('../index_1/')  # Reemplaza 'pagina_personalizada' con la URL que desees
    else:
        form = login()  # Utiliza el formulario 'login' aquí
    return render(request, 'login.html', {'form': form})  # Asegúrate de que el template sea 'login.html'

# Función para enviar correo de registro
def enviar_correo_registro(usuario):
    subject = '¡Bienvenido a nuestro sitio!'
    message = f'Tu nombre de usuario: {usuario.username}\nContraseña: ********\n'  # No incluyas la contraseña real aquí
    from_email = 'vipermxm@gmail.com'
    recipient_list = [usuario.email]
    send_mail(subject, message, from_email, recipient_list)



########correo############


class login(APIView):
    #encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

class index_1(APIView):
    template_name = "index_1.html"

    def get(self, request):
        return render(request, self.template_name)
    