from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def FirstApp(request):
     template = loader.get_template('first_page.html')
     return HttpResponse(template.render())