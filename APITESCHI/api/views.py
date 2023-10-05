# renderiza y redirige
from django.shortcuts import render, redirect
from rest_framework.views import APIView

# importo la bd de usuario
from .models import Usuario

# para los correos
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class login(APIView):
    # encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
        
        return render(request, self.template_name, {"error": ""})

    # metodo de envio de informacion para almacenar
    def post(self, request):
        try:
            if request.method == "POST":
                email = request.POST["email"]

                # Verifica si el correo ya existe en la base de datos
                if Usuario.objects.filter(correoElectronico=email).exists():
                    mensaje = "El correo electrónico ya está registrado. Por favor, usa otro correo."
                    # return render(request, 'login.html', {'mensaje': mensaje})
                    return render(request, self.template_name, {"error": mensaje})
                else:
                    if request.POST["password1"] == request.POST["password2"]:
                        print("hola registro")
                        user = Usuario(
                            nombreUsuario=request.POST["nombre"],
                            apellidoPaterno=request.POST["apellidoPaterno"],
                            apellidoMaterno=request.POST["apellidoMaterno"],
                            password=request.POST["password1"],
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

        except:
            return render(request, self.template_name, {"error": ""})


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



