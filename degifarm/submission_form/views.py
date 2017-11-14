from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.

def index(request):
  return render(request, 'submission_form/index.html', {})

def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      file_data = read_file(request.FILES['file'])
      return render(request, 'submission_form/sucess.html', {
        'file_data': file_data,
      })
  else:
    form = UploadFileForm()
  return render(request, 'submission_form/upload_file.html', {
    'form': form,
  })

def read_file(file_source):
  data = file_source.name + ' : '
  for chunk in file_source.chunks():
    data = data + str(chunk)

  return data
