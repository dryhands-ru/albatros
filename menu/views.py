from django.shortcuts import render
from .models import *


def mainpage(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/top.html', context)

def page1(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes1.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page1.html', context)

def page2(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes2.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page2.html', context)

def page3(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes3.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page3.html', context)

def page4(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes4.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page4.html', context)

def page5(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes5.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page5.html', context)

def page6(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes6.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page6.html', context)

def page7(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes7.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page7.html', context)

def page8(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes8.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page8.html', context)

def page100(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes100.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page100.html', context)

def page101(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes101.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page101.html', context)

def page102(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes102.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page102.html', context)

def page103(request):
    context={}
    context['arrDishes'] = list(enumerate(Dishes103.objects.all()))
    context['title'] = Header.objects.all()[0].title
    context['background'] = Header.objects.all()[0].background
    context['top_pic'] = Header.objects.all()[0].top_pic
    context['menuitems'] = list(enumerate(MenuItem.objects.all(),1))
    context['horizontmenuitems'] = list(enumerate(MenuItemHorizont.objects.all(),100))

    return render(request, 'menu/page103.html', context)

