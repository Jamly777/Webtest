from django.shortcuts import render
from django.http import HttpRequest,HttpResponseRedirect,HttpResponse
from . import models
import json
from django import forms

# Create your views here.
def test(request):
    res=models.Test.objects.all()
    for i in range(len(res)):
        if res[i].name == 'Tim':
            print('yes')
        else:
            print('False')
    #models.Test.objects.create(name='Jamly',password='123456')
    return render(request,'3.html')

def bart(request):
    if request.method == 'POST':
        price=request.POST.getlist('')
        print(price)
    return render(request,'reword.html')

def testajax(request):
    code={}
    if request.method == 'POST':
        data=request.POST.get('name')
        print(data)
        if data !="":
            code['Code']='SUCCESS'
        return HttpResponse(json.dumps(code))


