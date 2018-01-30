# django module
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

# app module
from submission_form.forms import DistributionFilesForm
from submission_form.views.DistributionFileUploader import *
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.models import Distribution, Classification
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

# lib


class DistributionList(LoginRequiredMessageMixin, ListView):
  model = Distribution
  template_name = 'submission_form/upload_list.html'
  context_object_name = 'dist_list'

  def get_queryset(self):
    try:
      return Distribution.objects.filter(user_id = self.request.user)
    except Distribution.DoesNotExist:
      return None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # userにリーレーションされるStudentかTeacherのレコードを取得する
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is not None:
      context['classification'] = Classification.objects.filter(organization_id = user_info.organization_id)
    return context



class DistributionFilesView(LoginRequiredMessageMixin, FormView):
  form_class = DistributionFilesForm
  template_name = 'submission_form/upload_file.html'
  success_url = reverse_lazy('submission_form:upload_index') # urlsの項目からURLを生成するメソッド

  def get_form(self, form_class = None):
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is None:
      return DistributionFilesForm()   

    return DistributionFilesForm(org_id = user_info.organization_id) 

  def post(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    files = request.FILES.getlist('files')
    class_id = request.POST['classification']
    if form.is_valid():
      dist_uploader = DistributionUploader(files, class_id, request.user)
      dist_uploader.handle_uploaded_files()
      return self.form_valid(form)
    else:
      return self.form_invalid(form)


# メモリ展開されたバイトデータを文字列に変換する
def read_file(file_source):
  data = file_source.name + ' : '
  charcode=chardet.detect(file_source.read())
  for chunk in file_source.chunks():
    data = data + chunk.decode(charcode['encoding'])

  return data
