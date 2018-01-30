from django.views.generic.base import View
from django.http import HttpResponse, Http404

from submission_form.models import Distribution, Submission

import urllib

class DownloadView(View):
  def get(self, request, **kwargs):
    file = self.get_object(kwargs.get('pk'))
    try:
      response = HttpResponse(open(file.path, 'rb').read())
    except:
      raise Http404
    response['Content-Disposition'] = 'attachment; filename="{fn}"'.format(fn = urllib.parse.quote(file.name))
    return response

  def get_object(self, pk):
    return Distribution.objects.get(id = pk)

class DownloadSubView(DownloadView):
  def get_object(self, pk):
    return Submission.objects.get(id = pk)
