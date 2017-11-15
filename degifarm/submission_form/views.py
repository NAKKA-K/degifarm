from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.

def index(request):
  return render(request, 'submission_form/index.html', {})


def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      file_data = read_file(request.FILES['file']) # ファイル取得(メモリ展開状態)したものを、文字列に変換

      return render(request, 'submission_form/sucess.html', { # アップロード完了ページに遷移
        'file_data': file_data,
      })

  else:
    form = UploadFileForm()

  return render(request, 'submission_form/upload_file.html', {
    'form': form,
  })


# メモリ展開されたバイトデータを文字列に変換する
def read_file(file_source):
  data = file_source.name + ' : \n'
  for chunk in file_source.chunks():
    data = data + chunk.decode('utf-8')

  return data





