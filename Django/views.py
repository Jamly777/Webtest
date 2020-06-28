from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from urllib import parse
import requests
import json


def index(request):
    APIurl=' http://api.avatardata.cn/Weather/Query?key=ce2d260ee1e34aa796c78e03b4f7376c&cityname=成都'
    response=requests.get(APIurl)
    print(response.text)
    res=json.loads(response.text)
    result=res['result']

    realtime=result['realtime']
    realtime_wind=realtime['wind']
    realtime_city=realtime['city_name']

    life=result['life']
    life_date=life['date']
    life_info=life['info']
    kongtiao=life_info['kongtiao']
    sport=life_info['yundong']
    ziwaixian=life_info['ziwaixian']
    ganmao=life_info['ganmao']

    weather=result['weather']
    weather_info=weather[0]['info']
    day=weather_info['day']
    dawn=weather_info['dawn']
    night=weather_info['night']


    if request.method == 'GET':
        return render(request,'1.html',{'wind':realtime_wind,'city':realtime_city,
                                        'date':life_date,'kongtiao':kongtiao,
                                        'sport':sport,'ganmao':ganmao,
                                        'day':day,'dawn':dawn,'night':night})

def test(request):
    return render(request,'2.html')
