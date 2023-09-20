from django.shortcuts import render
from rest_framework.views import APIView
import requests

class login(APIView):
    #encapsulo el login para su llamado
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

class index_1(APIView):
    template_name = "index_1.html"

    def get(self, request):
        return render(request, self.template_name)
    