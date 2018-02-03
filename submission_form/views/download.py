from django.views.generic.base import View
from django.http import HttpResponse, Http404

from submission_form.models import Distribution, Submission
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

import urllib

class DownloadView(View):
  def get(self, request, **kwargs):
    file = self.get_object(kwargs.get('pk'))
    try:
      response = HttpResponse(open(file.path, 'rb').read())
    except:
      raise Http404 #ファイルが存在しない
    response['Content-Disposition'] = 'attachment; filename="{fn}"'.format(fn = urllib.parse.quote(file.name))
    return response

  def get_object(self, pk):
    return None


class DownloadDistView(DownloadView):
  def get_object(self, pk):
    """所属Orgの配布物のみ取得できる"""
    distribution = Distribution.objects.get(id = pk)
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info.organization_id == distribution.organization_id:
      return distribution
    raise Http404


class DownloadSubView(DownloadView):
  def get_object(self, pk):
    """所属Orgかつ、自分の提出物か先生のみ取得できる"""
    submission = Submission.objects.get(id = pk)
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info.organization_id == submission.organization_id\
       and (self.request.user == submission.user_id\
       or StudentOrTeacherGetter.is_teacher(self.request.user)):
      return submission
    raise Http404

