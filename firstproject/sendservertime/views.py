from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,time
# Create your views here.
def sendtime(request):
    s=f'''<h1>{datetime.date(datetime.now())}<h1>
    <p>{datetime.now().time().strftime("%H:%M")}<p>'''
    return HttpResponse(s)
