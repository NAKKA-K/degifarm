from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^task/$', views.TaskHomeView.as_view(), name = 'task_index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),
  url(r'^upload/$', views.UploadList.as_view(), name = 'Upload_index')
]
