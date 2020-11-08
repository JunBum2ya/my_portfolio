from django.shortcuts import render,redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *
from main.views import is_active
from member.models import User
import datetime
import urllib
import os
import mimetypes

# Create your views here.
def index(request):
    boards=Board.objects.all().order_by('-id')
    context = {"boards":boards}
    context.update(is_active(request.session))
    return render(request,"board/index.html",context)

def paging(request,tableid):
    Table=Board.objects.all().order_by('-id')
    paging=Paginator(Table,10)
    context={"Table":paging.page(tableid)}
    context.update(is_active(request.session))
    return render(request,"board/paging.html",context)

def create(request):
    if 'user_id' in request.session.keys():
        user_name=request.session['user_name']
        content = {"user_name":user_name,"is_active":True}
    else:
        return redirect('/member/signin')
    return render(request,'board/add.html',content)

def add(request):
    board_title=request.POST['title']
    board_detail=request.POST['detail']
    if 'fileInput' in request.POST.keys():
        file=None
    else:
        file=request.FILES['fileInput']
    user_name=request.session['user_id']
    board_count=0
    board_create_date=datetime.datetime.now()
    board_update_date=datetime.datetime.now()
    board_user=User.objects.get(user_id=request.session['user_id'])
    board_user_name=request.session['user_name']
    board=Board(title=board_title,detail=board_detail,count=board_count,create_date=board_create_date,
                update_date=board_update_date,user_id=board_user,user_name=board_user_name,attachment=file)
    board.save()
    grant=is_active(request.session)
    return redirect('/board/paging/1')
    
def detail(request,boardid):
    if 'user_id' in request.session.keys():
        board=Board.objects.get(id=boardid)
        board.count=board.count+1
        board.save()
        is_active=request.session['user_id']==board.user_id.user_id
        replies=Reply.objects.all().order_by('-id').filter(board_id=boardid)
        context={'is_active':is_active,'board':board,'replies':replies}
        return render(request,"board/detail.html",context)
    else:
        return redirect('/member/signin')

def reply(request,boardid):
    if request.method=="POST":
        detail=request.POST['commentContent']
        writer=User.objects.get(user_id=request.session['user_id'])
        board=Board.objects.get(id=boardid)
        reply=Reply(board_id=board,user_id=writer,detail=detail)
        reply.save()
    return HttpResponseRedirect(reverse('board_detail',args=[boardid]))
    

def download(request,boardid):
    board=Board.objects.get(id=boardid)
    filePath=os.path.join(settings.MEDIA_ROOT,board.attatchment.name)
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fh:
            quote_file_url = urllib.parse.quote(board.attatchment.name.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(filePath)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404
        #downloadFile=open(filePath,'rb')
        #response=HttpResponse(downloadFile.read())
        #response['Content-Disposition']='attachment; filename='+os.path.basename(filePath)
        #return response
    #else:
        #return render(request,'board/index.html')

def update(request,boardid):
    board=Board.objects.get(id=boardid)
    is_active=request.session['user_id']==board.user_id.user_id
    context={'is_active':is_active,'board':board}
    return render(request,"board/update.html",context)

def change(request,boardid):
    board=Board.objects.get(id=boardid)
    board.title=request.POST['title']
    board.detail=request.POST['detail']
    temp_Path=os.path.join(settings.MEDIA_ROOT,board.attachment.name)
    if 'fileInput' in request.POST.keys():
        file=None
        is_file=False
    else:
        file=request.FILES['fileInput']
        is_file=True
    if os.path.isfile(temp_Path) and is_file:
        os.remove(temp_Path)
        board.attachment=file
    board.update_date=datetime.datetime.now()
    board.save()
    return redirect('/board/paging/1')
    #return redirect(reverse('board_index'))

def delete(request,boardid):
    board = Board.objects.get(id=boardid)
    filePath=os.path.join(settings.MEDIA_ROOT,board.attachment.name)
    if os.path.isfile(filePath):
        os.remove(filePath)
    board.delete()
    return redirect('/board/paging/1')

def search(request):
    if request.method=="GET":
        boards=Board.objects.all().order_by('-id')
        q=request.GET.get('q',"")
        if q:
            board=boards.filter(title_incontains=q)
            return render()
        context = {"boards":boards}
        context.update(is_active(request.session))
        return render(request,"board/search.html",context)