from django.shortcuts import render
from django.http import HttpResponse 
from datetime import datetime

def sayhello(resquest):
    return HttpResponse('sayhello......')
    
def hello2(resquest, username):
    now = datetime.now()
    return render(resquest, 'hello3.html', {'username':username, 'now':now})
