from django.shortcuts import render
from rest_framework.views import APIView
import requests

class sing_in(APIView):
    template_name = "sing_in.html"

    def get(self, request):
        return render(request, self.template_name)

    