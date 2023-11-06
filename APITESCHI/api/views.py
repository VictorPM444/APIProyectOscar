# renderiza y redirige
from django.shortcuts import render, redirect
from rest_framework.views import APIView
import random
import string
# importo la bd de usuario
from .models import Usuario


# importaciones para vsc
from .models import Formulario  # Asegúrate de importar tu modelo
import csv

# importaciones para graficos
from django.db.models import Count



# para los correos
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


from django.contrib.auth.hashers import (
    make_password,
)  # Importa la función make_password


from django.contrib.auth.hashers import check_password


class login(APIView):
    template_name = "login.html"

    def post(self, request):
        ###########Importacion de datos desde CSV###################
        """ archivo_csv = 'C:/Users/Victor Patiño Mejia/Desktop/Respuestas.csv'  # Ruta al archivo CSV que deseas importar

        with open(archivo_csv, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                nuevo_registro = Formulario(
                    pregunta1=row['¿Qué busca en una tienda online?'],
                    pregunta2=row['¿Qué forma de pago desea tener en una tienda online?'],
                    pregunta3=row['¿En que dispositivos visita mas una tienda online?'],
                    pregunta4=row['En una tienda online de calzado, ¿Qué tipo de calzado busca con mas frecuencia?'],
                    pregunta5=row['¿Qué métodos de búsqueda prefiere para un tienda de calzado online? '],
                    pregunta6=row['¿Se basa de las opiniones y calificaciones de los demás para definir si comprar o no un producto online?'],
                    pregunta7=row['¿Cómo prefieres la vista de productos online?'],
                    pregunta8=row['¿Qué le gustaría tener por el uso y compra de productos online?'],
                    pregunta9=row['¿Te gustaría recibir notificaciones o avisos sobre ofertas y promociones? '],
                    pregunta10=row['¿Qué método de registro prefieres en tiendas online?'],
                    # Asigna los campos y columnas correspondientes
                )
                nuevo_registro.save()
        return render(request, 'home.html') """
        ###########Importacion de datos desde CSV###################


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
    
class graficas_powerbi(APIView):
    template_name = "graficas_powerbi.html"

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
    
class graficas_formulario(APIView):
    template_name = "graficas_formulario.html"

    def post(self, request):
        return render(request, self.template_name)

    
    def get(self, request):

        # Pregunta 1
        respuestas1 = Formulario.objects.values('pregunta1').annotate(total=Count('pregunta1'))
        etiquetas1 = [respuesta['pregunta1'] for respuesta in respuestas1]
        valores1 = [respuesta['total'] for respuesta in respuestas1]

        # Pregunta 2
        respuestas2 = Formulario.objects.values('pregunta2').annotate(total=Count('pregunta2'))
        etiquetas2 = [respuesta['pregunta2'] for respuesta in respuestas2]
        valores2 = [respuesta['total'] for respuesta in respuestas2]

        # Pregunta 3
        respuestas3 = Formulario.objects.values('pregunta3').annotate(total=Count('pregunta3'))
        etiquetas3 = [respuesta['pregunta3'] for respuesta in respuestas3]
        valores3 = [respuesta['total'] for respuesta in respuestas3]

        # Pregunta 4
        respuestas4 = Formulario.objects.values('pregunta4').annotate(total=Count('pregunta4'))
        etiquetas4 = [respuesta['pregunta4'] for respuesta in respuestas4]
        valores4 = [respuesta['total'] for respuesta in respuestas4]

        # Pregunta 5
        respuestas5 = Formulario.objects.values('pregunta5').annotate(total=Count('pregunta5'))
        etiquetas5 = [respuesta['pregunta5'] for respuesta in respuestas5]
        valores5 = [respuesta['total'] for respuesta in respuestas5]

        # Pregunta 6
        respuestas6 = Formulario.objects.values('pregunta6').annotate(total=Count('pregunta6'))
        etiquetas6 = [respuesta['pregunta6'] for respuesta in respuestas6]
        valores6 = [respuesta['total'] for respuesta in respuestas6]

        # Pregunta 7
        respuestas7 = Formulario.objects.values('pregunta7').annotate(total=Count('pregunta7'))
        etiquetas7 = [respuesta['pregunta7'] for respuesta in respuestas7]
        valores7 = [respuesta['total'] for respuesta in respuestas7]

        # Pregunta 8
        respuestas8 = Formulario.objects.values('pregunta8').annotate(total=Count('pregunta8'))
        etiquetas8 = [respuesta['pregunta8'] for respuesta in respuestas8]
        valores8 = [respuesta['total'] for respuesta in respuestas8]

        # Pregunta 9
        respuestas9 = Formulario.objects.values('pregunta9').annotate(total=Count('pregunta9'))
        etiquetas9 = [respuesta['pregunta9'] for respuesta in respuestas9]
        valores9 = [respuesta['total'] for respuesta in respuestas9]

        # Pregunta 10
        respuestas10 = Formulario.objects.values('pregunta10').annotate(total=Count('pregunta10'))
        etiquetas10 = [respuesta['pregunta10'] for respuesta in respuestas10]
        valores10 = [respuesta['total'] for respuesta in respuestas10]


    
        # Pasa los datos a la plantilla
        return render(request, self.template_name, {'etiquetasPregunta1': etiquetas1, 
                                                    'valoresPregunta1': valores1,
                                                   'etiquetasPregunta2': etiquetas2,
                                                   'valoresPregunta2': valores2,
                                                   'etiquetasPregunta3': etiquetas3,
                                                   'valoresPregunta3': valores3,
                                                   'etiquetasPregunta4': etiquetas4,
                                                   'valoresPregunta4': valores4,
                                                   'etiquetasPregunta5': etiquetas5,
                                                   'valoresPregunta5': valores5,
                                                   'etiquetasPregunta6': etiquetas6,
                                                   'valoresPregunta6': valores6,
                                                   'etiquetasPregunta7': etiquetas7,
                                                   'valoresPregunta7': valores7,
                                                   'etiquetasPregunta8': etiquetas8,
                                                   'valoresPregunta8': valores8,
                                                   'etiquetasPregunta9': etiquetas9,
                                                   'valoresPregunta9': valores9,
                                                   'etiquetasPregunta10': etiquetas10,
                                                   'valoresPregunta10': valores10})

    
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
