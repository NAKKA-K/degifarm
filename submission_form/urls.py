from django.conf.urls import url
from . import views

app_name = 'submission_form'

urlpatterns = [
  # 提出物
  url(r'^$', views.HomeView.as_view(), name = 'index'),
  url(r'^list/$', views.TaskHomeView.as_view(), name = 'list'),
  url(r'^upload/list/$', views.UploadList.as_view(), name = 'upload_index'),
  url(r'^upload/form/$', views.UploadFilesView.as_view(), name = 'upload_form'),
  url(r'^download/(?P<pk>.*)/$',views.DownloadSubView.as_view(), name='sub_download'),
  url(r'^delete/(?P<pk>.*)/$',views.DeleteSubmissionView.as_view(), name='sub_delete'),

  # 先生のみアクセス可
  url(r'^task/create/$', views.TaskCreateView.as_view(), name = 'task_create'),
  url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name = 'task_detail'),
  url(r'^task/(?P<pk>[0-9]+)/edit/$', views.TaskEditView.as_view(), name = 'task_edit'),
  url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name = 'task_delete'),

  # 配布物
  url(r'^distribution/$', views.DistListView.as_view(), name='dist_index'),
  url(r'^distribution/(?P<category_pk>[0-9]+)/$', views.DistClassListView.as_view(), name='dist_category'),
  url(r'^distribution/create/$', views.DistUploadView.as_view(), name='dist_create'),
  url(r'^distribution/update/(?P<pk>.*)/$',views.DistUpdateView.as_view(), name='dist_update'),
  url(r'^distribution/delete/(?P<pk>.*)/$',views.DistDeleteView.as_view(), name='dist_delete'),
  url(r'^distribution/download/(?P<pk>.*)/$',views.DownloadDistView.as_view(), name='dist_download'),

  # 分類(カテゴリ)
  url(r'^category/$', views.CategoryIndexView.as_view(), name='category_index'),
  url(r'^category/create/$', views.CategoryCreateView.as_view(), name='category_create'),
  url(r'^category/update/(?P<pk>[0-9]+)/$', views.CategoryUpdateView.as_view(), name='category_update'),
  url(r'^category/delete/(?P<pk>[0-9]+)/$', views.CategoryDeleteView.as_view(), name='category_delete'),

  # 分類(カテゴリ)
  url(r'^group/$', views.GroupIndexView.as_view(), name='group_index'),
  url(r'^group/create/$', views.GroupCreateView.as_view(), name='group_create'),
  url(r'^group/update/(?P<pk>[0-9]+)/$', views.GroupUpdateView.as_view(), name='group_update'),
  url(r'^group/delete/(?P<pk>[0-9]+)/$', views.GroupDeleteView.as_view(), name='group_delete'),


  url(r'^download/zip/$', views.DownloadZipView.as_view(), name='download_zip'),
]
