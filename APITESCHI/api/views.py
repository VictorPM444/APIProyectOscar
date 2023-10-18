# renderiza y redirige
from django.shortcuts import render, redirect
from rest_framework.views import APIView
import random
import string
# importo la bd de usuario
from .models import Usuario


# para los correos
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.contrib.auth.hashers import (
    make_password,
)  # Importa la función make_password

from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.hashers import check_password


class login(APIView):
    template_name = "login.html"

    def post(self, request):
        if "Inicio" in request.POST:
            # Procesar Login
            email = request.POST.get("email22")
            password1 = request.POST.get("password22")

            # Buscar un usuario con el correo electrónico proporcionado
            try:
                usuario = Usuario.objects.get(correoElectronico=email)  # , password=password1
                # usuario = authenticate(request, correoElectronico=email, password=password1)
                valorObtenido = usuario.correoElectronico
            except Usuario.DoesNotExist:
                valorObtenido = None

            # usuario = authenticate(request, correElectronico=email, password=password1)

            contra = usuario.password

            if valorObtenido is not None:
                # La contraseña es correcta, inicia sesión
                # login(request, usuario)
                if check_password(password1, contra):
                    return redirect(
                        "home"
                    )  # Redirige a la página 'home' después del inicio de sesión
                else:
                    mensaje = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
                    return render(request, self.template_name, {"error": mensaje})

            else:
                mensaje = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
                return render(request, self.template_name, {"error": mensaje})
            # Lógica de login aquí

        else:
            # Procesar registro
            try:
                if "Registro" in request.POST:
                    email = request.POST["email"]

                    # Verifica si el correo ya existe en la base de datos
                    if Usuario.objects.filter(correoElectronico=email).exists():
                        mensaje = "El correo electrónico ya está registrado. Por favor, usa otro correo."
                        # return render(request, 'login.html', {'mensaje': mensaje})
                        return render(request, self.template_name, {"error": mensaje})
                    else:
                        if request.POST["password1"] == request.POST["password2"]:
                            user = Usuario(
                                nombreUsuario=request.POST["nombre"],
                                username=request.POST["username"],
                                apellidoPaterno=request.POST["apellidoPaterno"],
                                apellidoMaterno=request.POST["apellidoMaterno"],
                                password=make_password(request.POST["password1"]),
                                correoElectronico=request.POST["email"],
                                numeroTelefonico=request.POST["numeroTelefono"],
                            )
                            user.save()

                            # Luego, prepara y envía el correo electrónico
                            subject = "Registro Exitoso"
                            from_email = "vipermxm@gmail.com"
                            recipient_list = [request.POST["email"]]

                            # Utiliza la plantilla HTML para el correo electrónico
                            html_message = render_to_string(
                                "bienvenida.html",
                                {
                                    "nombre": request.POST["nombre"]
                                    + " "
                                    + request.POST["apellidoPaterno"]
                                    + " "
                                    + request.POST["apellidoMaterno"]
                                },
                            )
                            # {{nombre}} es como se llama la variable que mandamos
                            # Envía el correo electrónico
                            send_mail(
                                subject,
                                strip_tags(html_message),
                                from_email,
                                recipient_list,
                                html_message=html_message,
                            )
                            return redirect("home")

                        else:
                            contra_diff = "La contraseña no es la misma. Por favor, reintente de nuevo."
                            return render(
                                request, self.template_name, {"error": contra_diff}
                            )

                    # Lógica de registro aquí
                return redirect(
                    "cart"
                )  # Redirige a la página deseada después del registro
            except:
                return render(request, self.template_name, {"error": ""})

    def get(self, request):
        return render(request, self.template_name)


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
        return render(request, "cart.html", {"usuarios": usuarios})
        # return render(request, self.template_name)

    # def vista_usuarios(request):
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
    
class recuperacion_contra(APIView):
    template_name = "recuperacion_contra.html"

    def post(self, request):
        if "Recuperacion" in request.POST:
            # Recuperar pasword
            email = request.POST["prueba"]
            # Verifica si el correo ya existe en la base de datos
            if Usuario.objects.filter(correoElectronico=email).exists():
                
                # Obtén un usuario específico por su correo electrónico
                usuario = Usuario.objects.get(correoElectronico=email)

                # Genera una contraseña aleatoria de 12 caracteres que incluye letras mayúsculas, letras minúsculas y dígitos
                nueva_contrasena = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        
                # Almacena la contraseña aleatoria como la nueva contraseña del usuario (debes cifrarla)
                usuario.password = make_password(nueva_contrasena)

                # Guarda el usuario en la base de datos para actualizar la contraseña
                usuario.save()
                
                # Luego, prepara y envía el correo electrónico
                subject = "Recuperacion de Contraseña"
                from_email = "vipermxm@gmail.com"
                recipient_list = [request.POST["prueba"]]

                # Utiliza la plantilla HTML para el correo electrónico
                html_message = render_to_string("correo_recuperacion.html",{
                                    "contrasena": " "
                                    + nueva_contrasena
                                },
                            )
                            # {{nombre}} es como se llama la variable que mandamos
                            # Envía el correo electrónico
                send_mail(subject,strip_tags(html_message),from_email,recipient_list,html_message=html_message,)
                return redirect("login")
        else:
            mensaje = "Su correo no existe"
            return render(request, self.template_name, {"mensajeo": mensaje})
        # Logica de recuperacion de pasword

    def get(self, request):
        return render(request, self.template_name)
