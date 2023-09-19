from django.shortcuts import render
#Hecho en clase para importar la APIView
from rest_framework.views import APIView
# Create your views here.

#Creacion de lista, con todo el index dentro
class Home(APIView):
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)