from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='board_index'),
    path('create',views.create,name='board_create'),
    path('create/add',views.add,name='board_add'),
    path('detail/<int:boardid>/',views.detail,name="board_detail"),
    path('detail/<int:boardid>/reply',views.reply,name="board_reply"),
    path('detail/<int:boardid>/download',views.download,name="board_download"),
    path('paging/<int:tableid>/',views.paging,name='board_paging'),
    path('update/<int:boardid>/',views.update,name="board_update"),
    path('update/<int:boardid>/change',views.change,name="board_change"),
    path('delete/<int:boardid>/',views.delete,name="board_delete"),
    path('search',views.search,name="board_search"),
]