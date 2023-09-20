from django.shortcuts import render
from rest_framework.views import APIView
import requests

class Home(APIView):
    template_name = "index.html"
    

    def get(self, request):
        return render(request, self.template_name)

    