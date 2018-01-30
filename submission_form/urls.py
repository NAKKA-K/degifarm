from django.conf.urls import url
from . import views

urlpatterns = [
  # 提出物
  url(r'^$', views.TaskHomeView.as_view(), name = 'index'),
  url(r'^upload/$', views.UploadList.as_view(), name = 'upload_index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),
  url(r'^submission/download/(?P<pk>.*)/$',views.DownloadSubView.as_view(), name='sub_download'),

  # 先生のみアクセス可
  url(r'^task/create/$', views.TaskCreateView.as_view(), name = 'task_create'),
  url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name = 'task_detail'),
  url(r'^task/(?P<pk>[0-9]+)/edit/$', views.TaskEditView.as_view(), name = 'task_edit'),
  url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name = 'task_delete'),

  # 配布物
  url(r'^distribution/$', views.FileIndexView.as_view(), name='dist_index'),
  url(r'^distribution/(?P<category_pk>[0-9]+)/$', views.FileCategoryView.as_view(), name='dist_category'),
  url(r'^distribution/create/$', views.FileCreateView.as_view(), name='dist_create'),
  url(r'^distribution/update/(?P<pk>.*)/$',views.FileUpdateView.as_view(), name='dist_update'),
  url(r'^distribution/delete/(?P<pk>.*)/$',views.FileDeleteView.as_view(), name='dist_delete'),
  url(r'^distribution/download/(?P<pk>.*)/$',views.DownloadView.as_view(), name='dist_download'),

  # 分類(カテゴリ)
  url(r'^category/$', views.CategoryIndexView.as_view(), name='category_index'),
  url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
  url(r'^category/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(), name='category_update'),
  url(r'^category/delete/(?P<pk>[0-9]+)/$', views.CategoryDeleteView.as_view(), name='category_delete'),
]
