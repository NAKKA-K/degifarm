from django.views.generic.list import ListView

from submission_form.models import Submission, Classification


class UploadList(ListView):
  model = Submission
  template_name = 'submission_form/upload_list.html'
  context_object_name = 'upload_list'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['classification'] = Classification.objects.all()
    return context
