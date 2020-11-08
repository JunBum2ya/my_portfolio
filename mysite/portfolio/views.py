from django.shortcuts import render
from main.views import is_active
from member.models import User
import pandas as pd

# Create your views here.
def index(request):
    context=is_active(request.session)
    return render(request,'portfolio/index.html',context)

def career(request):
    context=is_active(request.session)
    return render(request,'portfolio/career.html',context)

def beacon(request):
    context=is_active(request.session)
    return render(request,'portfolio/beacon.html',context)  

def beacon_video(request):
    context=is_active(request.session)
    return render(request,'portfolio/beacon_video.html',context)

def pandas(request):
    qs=User.objects.all().values()
    df=pd.DataFrame(qs)
    print(df)
    context = {"is_active":is_active(request.session),"pandas":df.to_html()}
    return render(request,'portfolio/pandas.html',context)