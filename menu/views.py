from django.shortcuts import render
from .models import *


def mainpage(request):
    context={}
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['backgroundMain'] = Header.objects.all()[0].backgroundMain
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['image'] = MenuItem.objects.all()[0].image

    return render(request, 'menu/index.html', context)


def top(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/top.html', context)


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

def page4(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes4.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page4.html', context)

def page5(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes5.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page5.html', context)

def page6(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes6.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page6.html', context)

def page7(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes7.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page7.html', context)

def page8(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes8.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page8.html', context)

def page9(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes9.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page9.html', context)

def page10(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes10.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page10.html', context)

def page11(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes11.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page11.html', context)

def page12(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes12.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page12.html', context)

def page13(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes13.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page13.html', context)

def page14(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes14.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page14.html', context)

def page15(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes15.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page15.html', context)

def page16(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes16.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))

    return render(request, 'menu/page16.html', context)

