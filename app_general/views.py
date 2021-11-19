from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('จันทร์ไรเดอร์')

def about(request):
    return HttpResponse('เกี่ยวกับจันทร์ไรเดอร์')