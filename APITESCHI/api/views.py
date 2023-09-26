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
       

class home(APIView):
    template_name = "index_1.html"

    def get(self, request):
        return render(request, self.template_name)


class shop(APIView):
    template_name = "index_2.html"

    def get(self, request):
        return render(request, self.template_name)
    
class my_account(APIView):
    template_name= "my_account.html"

    def get(self, request):
        return render(request, self.template_name)
    
class about_us(APIView):
    template_name= "about_us.html"

    def get(self, request):
        return render(request, self.template_name)
    
class account_details(APIView):
    template_name= "account_details.html"

    def get(self, request):
        return render(request, self.template_name)
    
class addresses(APIView):
    template_name= "addresses.html"

    def get(self, request):
        return render(request, self.template_name)
    
class cart(APIView):
    template_name= "cart.html"

    def get(self, request):
        return render(request, self.template_name)
    
class compare(APIView):
    template_name= "compare.html"

    def get(self, request):
        return render(request, self.template_name)
    
class contact(APIView):
    template_name= "contact.html"

    def get(self, request):
        return render(request, self.template_name)
    
class downloads(APIView):
    template_name= "downloads.html"

    def get(self, request):
        return render(request, self.template_name)
    
class faq(APIView):
    template_name= "faq.html"

    def get(self, request):
        return render(request, self.template_name)
    
class heading(APIView):
    template_name= "heading.html"

    def get(self, request):
        return render(request, self.template_name)
    
class index_3(APIView):
    template_name= "index_3.html"

    def get(self, request):
        return render(request, self.template_name)
    
class index(APIView):
    template_name= "index.html"

    def get(self, request):
        return render(request, self.template_name)
    
class modals(APIView):
    template_name= "modals.html"

    def get(self, request):
        return render(request, self.template_name)
    
class order_list(APIView):
    template_name= "order_list.html"

    def get(self, request):
        return render(request, self.template_name)
    
class product_details(APIView):
    template_name= "product_details.html"

    def get(self, request):
        return render(request, self.template_name)
    
class register(APIView):
    template_name= "register.html"

    def get(self, request):
        return render(request, self.template_name)
    
class wishlist(APIView):
    template_name= "wishlist.html"

    def get(self, request):
        return render(request, self.template_name)
    
    
class shop_grid_no_sidebar(APIView):
    template_name= "shop_grid_no_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_grid_left_sidebar(APIView):
    template_name= "shop_grid_left_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_grid_right_sidebar(APIView):
    template_name= "shop_grid_right_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_grid_top_sidebar(APIView):
    template_name= "shop_grid_top_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_list_left_sidebar(APIView):
    template_name= "shop_list_left_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_list_no_sidebar(APIView):
    template_name= "shop_list_no_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_list_right_sidebar(APIView):
    template_name= "shop_list_right_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    
class shop_list_top_sidebar(APIView):
    template_name= "shop_list_top_sidebar.html"

    def get(self, request):
        return render(request, self.template_name)
    






