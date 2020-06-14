from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('top/', views.top, name='top'),
    path('1/', views.page1, name='page1'),
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
    path('4/', views.page4, name='page4'),
    path('5/', views.page5, name='page5'),
    path('6/', views.page6, name='page6'),
    path('7/', views.page7, name='page7'),
    path('8/', views.page8, name='page8'),
    path('9/', views.page9, name='page9'),
    path('10/', views.page10, name='page10'),
    path('11/', views.page11, name='page11'),
    path('12/', views.page12, name='page12'),
    path('13/', views.page13, name='page13'),
    path('14/', views.page14, name='page14'),
    path('15/', views.page15, name='page15'),
    path('16/', views.page16, name='page16'),
]