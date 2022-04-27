# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request, 'metronicIncludes/layout/master.html')

def page1(request):
    return render(request, 'metronicIncludes/pages/page-1.html')