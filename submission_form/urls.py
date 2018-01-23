from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.TaskHomeView.as_view(), name = 'index'),
  url(r'^upload/$', views.UploadList.as_view(), name = 'upload_index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),

  # 先生のみアクセス可
  url(r'^task/create/$', views.TaskCreateView.as_view(), name = 'task_create'),
]
