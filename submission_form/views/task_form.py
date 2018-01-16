# django module
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

# app module
from submission_form.forms import UploadFilesForm
from submission_form.views.FileUploader import FileUploader

# lib


# here views ============================================

class TaskHomeView(TemplateView):
  template_name = 'submission_form/task_home.html'


class UploadFilesView(FormView):
  form_class = UploadFilesForm
  template_name = 'submission_form/upload_file.html'
  success_url = reverse_lazy('submission_form:upload') # urlsの項目からURLを生成するメソッド

  def post(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    files = request.FILES.getlist('files')
    if form.is_valid():
      file_uploader = FileUploader(files)
      file_uploader.handle_uploaded_files()

      return render(request, 'submission_form/upload_success.html', { # アップロード完了ページに遷移
        'files_list': file_uploader.files_path_list,
      })
    else:
      return self.form_invalid(form)

# メモリ展開されたバイトデータを文字列に変換する
def read_file(file_source):
  data = file_source.name + ' : '
  charcode=chardet.detect(file_source.read())
  for chunk in file_source.chunks():
    data = data + chunk.decode(charcode['encoding'])

  return data
