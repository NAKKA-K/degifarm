from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView
from .forms import UploadFilesForm

# Create your views here.

def index(request):
  return render(request, 'submission_form/index.html', {})

class UploadFilesView(FormView):
  form_class = UploadFilesForm
  template_name = 'submission_form/upload_file.html'
  success_url = reverse_lazy('submission_form:upload') # urlsの項目からURLを生成するメソッド

  def post(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    files = request.FILES.getlist('files')
    if form.is_valid():
      files_data = []
      for f in files: # ファイルデータをリストに挿入
        files_data.append(read_file(f))
      return render(request, 'submission_form/upload_success.html', { # アップロード完了ページに遷移
        'files_data': files_data,
      })
    else:
      return self.form_invalid(form)

  # メモリ展開されたバイトデータを文字列に変換する
  def read_file(file_source):
    data = file_source.name + ' : \n'
    for chunk in file_source.chunks():
      data = data + chunk.decode('utf-8')

    return data





