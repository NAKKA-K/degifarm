from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^upload$', views.UploadFilesView.as_view(), name = 'upload')
]
