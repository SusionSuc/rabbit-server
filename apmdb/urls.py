from django.urls import path
from . import views
from .storage import uploadlog

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-log', uploadlog.upload_log, name='uploadlog')
]
