from django.views.generic.list import ListView

from submission_form.models import Submission

class UploadList(ListView):
  model = Submission
  template_name = 'submission_form/upload_list.html'
  context_object_name = 'upload_list'
