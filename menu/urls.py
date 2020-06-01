from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('1/', views.page1, name='page1'),
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
    path('4/', views.page4, name='page4'),
    path('5/', views.page5, name='page5'),
    path('6/', views.page6, name='page6'),
    path('7/', views.page7, name='page7'),
    path('8/', views.page8, name='page8'),
    path('100/', views.page100, name='page100'),
    path('101/', views.page101, name='page101'),
    path('102/', views.page102, name='page102'),
    path('103/', views.page103, name='page103'),
]