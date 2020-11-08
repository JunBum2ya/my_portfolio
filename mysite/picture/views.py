from django.shortcuts import render
from main.views import is_active
# Create your views here.

def index(request):
    context=is_active(request.session)
    return render(request,'picture/index.html',context)