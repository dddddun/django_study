from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요~~~~~~ 이거슨~~~~~ 테스트페이지 이지롱")

# Create your views here.