from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    response='<h1>Abdou aw yselem 3lik sa7beyyy<h1>'
    return HttpResponse(response)


