from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='main_index'),
    path('properties',views.properties,name='main_properties'),
    path('list',views.list,name='main_list'),
    path('ex1',views.ex1,name='main_ex1'),
    path('ex2',views.ex2,name='main_ex2'),
    path('ex3',views.ex3,name='main_ex3'),
    path('ex5',views.ex5,name='main_ex5'),
    path('ex6',views.ex6,name='main_ex6'),
]
