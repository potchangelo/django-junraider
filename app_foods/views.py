from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def foods(request):
    return HttpResponse('เมนูอร่อย ส่งบ่อย ส่งแม่น By Junraider')

def food(request):
    return HttpResponse('รายละเอียดของเมนูนี้')