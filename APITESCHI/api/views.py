from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm
import requests
from django.http import HttpResponse

#def login(request):
 #   return render(request, 'login.html',{
  #      'form': UserCreationForm
   # })

   # if request.method == 'GET':
        # Realizar acciones para solicitudes GET
    #    return HttpResponse('Esta es una solicitud GET')

    #elif request.method == 'POST':
        # Realizar acciones para solicitudes POST
     #   return HttpResponse('Esta es una solicitud POST')

    # Otras acciones para otros métodos HTTP

    #return HttpResponse('Esta es una solicitud diferente de GET y POST')


#def hello(request):
 #   return render(request, 'login.html')


#class login(APIView):
    #encapsulo el login para su llamado
 #   template_name = "login.html"

  #  def get(self, request):
   #     if request.method == 'GET':
    #        print ('enviando formulario')
     #   else:
      #       print(request.POST)
       #      print ('obteniendo datos')
        #return render(request, self.template_name), {
         #   'form': UserCreationForm
        #}

#def login(request):
 #   if requests.method == 'GET':
  #          print ('enviando formulario')
   # else:
    #        print ('obteniendo datos')
    #return render(request, 'login.html')



class login(APIView):
    #encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
   #     if request.method == 'GET':
    #        print ('enviando formulario')
     #   else:
      #       print(request.POST)
       #      print ('obteniendo datos')
        return render(request, self.template_name) 
    #{
         #   'form': UserCreationForm
        #}

class index_1(APIView):
    template_name = "index_1.html"

    def get(self, request):
        return render(request, self.template_name)


class index_2(APIView):
    template_name = "index_2.html"

    def get(self, request):
        return render(request, self.template_name)
    
