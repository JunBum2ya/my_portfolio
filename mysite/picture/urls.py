from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='picture_index'),
]