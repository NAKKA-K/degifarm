from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.TaskHomeView.as_view(), name = 'index'),
  url(r'^upload/$', views.UploadList.as_view(), name = 'upload_index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),
  url(r'^distribution/$', views.FileIndexView.as_view(), name='dist_index'),
  url(r'^distribution/$',views.FileCategoryView.as_view(), name='dist_category'),

  # 先生のみアクセス可
  url(r'^task/create/$', views.TaskCreateView.as_view(), name = 'task_create'),
  url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name = 'task_detail'),
  url(r'^task/(?P<pk>[0-9]+)/edit/$', views.TaskEditView.as_view(), name = 'task_edit'),
  url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name = 'task_delete'),

  url(r'^file/category/(?P<category_pk>[0-9]+)/$',views.FileCategoryView.as_view(), name='dist_category'),
  url(r'^distribution/create/$', views.FileCreateView.as_view(), name='dist_create'),
  url(r'^distribution/create/(?P<classfi_pk>[0-9]+)/$', views.FileCreateView.as_view(), name='dist_create'),
  url(r'^distribution/update/(?P<pk>[0-9]+)/$',views.FileUpdateView.as_view(), name='dist_update'),
  url(r'^disribution/delete/(?P<pk>[0-9]+)/$',views.FileDeleteView.as_view(), name='dist_delete'),

  
  # 分類のCRUD
  url(r'^category/$',
      views.CategoryIndexView.as_view(), name='category_index'),
  url(r'^category/create/$',
      views.CategoryCreateView.as_view(), name='category_create'),
  url(r'^category/update/(?P<pk>[0-9]+)/$',
      views.CategoryUpdateView.as_view(), name='category_update'),
  url(r'^category/delete/(?P<pk>[0-9]+)/$',
      views.CategoryDeleteView.as_view(), name='category_delete'),

]
