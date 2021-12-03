from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('<h1>จันทร์ไรเดอร์</h1>')

def about(request):
    return HttpResponse('เกี่ยวกับจันทร์ไรเดอร์')