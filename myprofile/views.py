from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def top(request):
    return HttpResponse('トップページ')


def resume(request):
    return HttpResponse('職務経歴ページです')
