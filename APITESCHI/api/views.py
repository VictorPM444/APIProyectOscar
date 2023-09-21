#renderiza y redirige
from django.shortcuts import render,redirect
from rest_framework.views import APIView
#importo la bd de usuario
from .models import Usuario
#para los correos
from django.core.mail import send_mail



class login(APIView):
    #encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)
     
    #metodo de envio de informacion para almacenar
    def post(self, request):
        try:
            user=Usuario(
                nombreUsuario=request.POST["nombre"],
                apellidoPaterno=request.POST["apellidoPaterno"],
                apellidoMaterno=request.POST["apellidoMaterno"],
                password=request.POST["password1"],
                correoElectronico=request.POST["email"],
                numeroTelefonico=request.POST["numeroTelefono"]
            )
            user.save()
            subject = 'Gracias por su registro '+request.POST["nombre"]
            message = 'Bienvenido seas '+request.POST["nombre"]+' '+request.POST["apellidoPaterno"]+' '+request.POST["apellidoMaterno"]+' '+'esperamos encuentres todo lo que buscas en calzado "Viper"'
            from_email = 'vipermxm@gmail.com'
            recipient_list = [request.POST["email"]]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('index_1')
        except:
            return render(request, self.template_name,{"error":""})
       

class index_1(APIView):
    template_name = "index_1.html"

    def get(self, request):
        return render(request, self.template_name)


class index_2(APIView):
    template_name = "index_2.html"

    def get(self, request):
        return render(request, self.template_name)
    





