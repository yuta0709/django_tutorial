from django.http import HttpResponse
from django.urls import path
from .views import top, resume

urlpatterns = [
    path('', top),
    path('resume/', resume)
]
