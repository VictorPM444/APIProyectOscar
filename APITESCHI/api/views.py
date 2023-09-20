from django.shortcuts import render
from rest_framework.views import APIView

from django.core.mail import send_mail

import requests

class login(APIView):
    #encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)
    
#VISTA

subject = 'Asunto del Correo'
message = 'Este es el contenido del correo.'
from_email = 'vipermxm@gmail.com'
recipient_list = ['victorpmejia2701@gmail.com']

send_mail(subject, message, from_email, recipient_list)

    