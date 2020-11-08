from django.shortcuts import render

# Create your views here.
def is_active(session):
    is_active=False
    if 'user_id' in session.keys():
        is_active=True
        user_name=session['user_name']
        context = {"is_active":is_active,"session_name":user_name}
    else:
        context={"is_active":is_active}
    return context

def index(request):
    context=is_active(request.session)
    return render(request,'main/index.html',context)

def properties(request):
    return render(request,'main/seoul_properties.html')

def list(request):
    return render(request,'main/list_contents.html')

def ex1(request):
    return render(request,'main/ex1.html')

def ex2(request):
    return render(request,'main/ex2.html')

def ex3(request):
    return render(request,'main/ex3.html')

def ex5(request):
    return render(request,'main/ex5.html')

def ex6(request):
    return render(request,'main/ex6.html')