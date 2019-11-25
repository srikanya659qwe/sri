from django.shortcuts import render
from django.http import HttpResponse
import datetime
def showmsg(request):
	return HttpResponse("<h1>hai this is srikanya</h1>")

def index(request):
	tm=datetime.datetime.now()
	return HttpResponse("<h2>hai time now is %s</h2>" %tm)

def signup(request):
	return render(request,'mystore/signup.html')
def register(request):
	return render(request,'mystore/register.html')
def sri1(request):
	content={'name':'srikanya'}
	return render(request,'mystore/name.html',content)
def sri2(request):
	content={'name':'srikanya','dist':'srikakulam'}
	return render(request,'mystore/name2.html',content)
