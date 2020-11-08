from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='porfolio_index'),
    path('career',views.career,name='porfolio_career'),
    path('project/beacon',views.beacon,name="portfolio_beacon"),
    path('project/beacon/video',views.beacon_video,name="portfolio_beacon_video"),
    path('project/pandas',views.pandas,name="portfolio_pandas"),
]