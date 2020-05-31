from django.shortcuts import render
from .models import *


def mainpage(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/index.html', context)


def page1(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes1.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page1.html', context)

def page2(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes2.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page2.html', context)

def page3(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes3.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page3.html', context)