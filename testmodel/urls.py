from django import urls
from django.urls import path,re_path
from . import views

urlpatterns=[
    path('test',views.test),
    path('reword/',views.bart),
    path('testajax/',views.testajax),
]