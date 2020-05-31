from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('1/', views.page1, name='page1'),
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
]