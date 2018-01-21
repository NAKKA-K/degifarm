from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.TaskHomeView.as_view(), name = 'index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),
  url(r'^upload/$', views.UploadList.as_view(), name = 'upload_index')
]
