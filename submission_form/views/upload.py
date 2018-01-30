# django module
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

# app module
from submission_form.forms import UploadFilesForm
from submission_form.views.FileUploader import FileUploader
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.models import Submission, Classification
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

# lib


class UploadList(LoginRequiredMessageMixin, ListView):
  model = Submission
  template_name = 'submission_form/upload_list.html'
  context_object_name = 'upload_list'

  def get_queryset(self):
    try:
      return Submission.objects.filter(user_id = self.request.user)
    except Submission.DoesNotExist:
      return None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # userにリーレーションされるStudentかTeacherのレコードを取得する
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is not None:
      context['classification'] = Classification.objects.filter(organization_id = user_info.organization_id)
    return context



class UploadFilesView(LoginRequiredMessageMixin, FormView):
  form_class = UploadFilesForm
  template_name = 'submission_form/upload_file.html'
  success_url = reverse_lazy('submission_form:upload_index') # urlsの項目からURLを生成するメソッド

  def get_form(self, form_class = None):
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is None:
      return UploadFilesForm()   

    return UploadFilesForm(org_id = user_info.organization_id) 

  def post(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    files = request.FILES.getlist('files')
    class_id = request.POST['classification']
    if not bool(form.errors): # form.__init__をオーバーライドした場合に、is_boundがfalseになってしまうためis_validではだめ
      file_uploader = FileUploader(files, class_id, request.user)
      file_uploader.handle_uploaded_files()
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
