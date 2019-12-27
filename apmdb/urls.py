from django.urls import path
from . import views
from .storage import uploadlog
from .query import pagespeed

urlpatterns = [
    path('', views.index),
    path('upload-log', uploadlog.upload_log),
    path('page-speed/all-page', pagespeed.all_page),
    path('page-speed/speed-list', pagespeed.speed_list)
]
