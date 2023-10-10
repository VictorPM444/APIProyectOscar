# renderiza y redirige
from django.shortcuts import render, redirect
from rest_framework.views import APIView

# importo la bd de usuario
from .models import Usuario


# para los correos
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.contrib.auth.hashers import make_password  # Importa la función make_password


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


class login(APIView):
    template_name = "login.html"

    def post(self, request):
        if "Inicio de Sesión" in request.POST:
            email = request.POST.get('email22')
            password1 = request.POST.get('password22')

            # Buscar un usuario con el correo electrónico proporcionado
            try:
                usuario = Usuario.objects.get(correoElectronico=email)
            except Usuario.DoesNotExist:
                usuario = None

            if usuario is not None and usuario.password == password1:
                # La contraseña es correcta, inicia sesión
                login(request, usuario)
                return redirect('home')  # Redirige a la página 'home' después del inicio de sesión
            else:
                mensaje = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
                return render(request, self.template_name, {'error': mensaje})
        else:
            # Procesar registro
            # ...
            # Lógica de registro aquí
            return redirect('cart')  # Redirige a la página deseada después del registro

    def get(self, request):
        return render(request, self.template_name, {'form': AuthenticationForm()})


class home(APIView):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)


class my_account(APIView):
    template_name = "my_account.html"

    def get(self, request):
        return render(request, self.template_name)


class about_us(APIView):
    template_name = "about_us.html"

    def get(self, request):
        return render(request, self.template_name)


class account_details(APIView):
    template_name = "account_details.html"

    def get(self, request):
        return render(request, self.template_name)


class addresses(APIView):
    template_name = "addresses.html"

    def get(self, request):
        return render(request, self.template_name)


class cart(APIView):
    template_name = "cart.html"

    def get(self, request):
        usuarios = Usuario.objects.all()
        return render(request, 'cart.html', {'usuarios': usuarios})
        #return render(request, self.template_name)
    
    #def vista_usuarios(request):
     #   usuarios = Usuario.objects.all()
      #  return render(request, 'cart.html', {'usuarios': usuarios})


class order_list(APIView):
    template_name = "order_list.html"

    def get(self, request):
        return render(request, self.template_name)


class wishlist(APIView):
    template_name = "wishlist.html"

    def get(self, request):
        return render(request, self.template_name)


class shop(APIView):
    template_name = "shop.html"

    def get(self, request):
        return render(request, self.template_name)


class checkout_complate(APIView):
    template_name = "checkout_complate.html"

    def get(self, request):
        return render(request, self.template_name)


class checkout_1(APIView):
    template_name = "checkout_1.html"

    def get(self, request):
        return render(request, self.template_name)


class checkout_2(APIView):
    template_name = "checkout_2.html"

    def get(self, request):
        return render(request, self.template_name)


class checkout_4(APIView):
    template_name = "checkout_4.html"

    def get(self, request):
        return render(request, self.template_name)


class checkout_5(APIView):
    template_name = "checkout_5.html"

    def get(self, request):
        return render(request, self.template_name)







