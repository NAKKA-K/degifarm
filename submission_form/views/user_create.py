from django.views.generic.base import TemplateView
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import Http404

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

import hashlib


class LinkUserCreateView(TemplateView):
  template_name = 'link_to_user_create.html'

  def get(self, request, **kwargs):
    if not request.user.is_authenticated:
      raise Http404

    if not StudentOrTeacherGetter.is_teacher(request.user):
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is None:
      return context

    # URL/accounts/create/<uuid>/<uuid+teacher or uuid+student>
    if self.request.is_secure():
      protocol = 'https'
    else:
      protocol = 'http'
    domain = get_current_site(self.request).domain
    url = "{}://{}".format(protocol, domain)
    
    teacher_hash = hashlib.sha224(str(user_info.organization_id.id).encode('utf-8'))
    teacher_hash.update('teacher'.encode('utf-8'))
    teacher_hash = teacher_hash.hexdigest() 

    student_hash = hashlib.sha224(str(user_info.organization_id.id).encode('utf-8'))
    student_hash.update('student'.encode('utf-8'))
    student_hash = student_hash.hexdigest()


    context['teacher_url'] = "{}{}".format(url,
      reverse('user_create', kwargs = {
        'uuid': user_info.organization_id.id,
        'uuid_hash': teacher_hash
      })
    )

    context['student_url'] = "{}{}".format(url,
      reverse('user_create', kwargs = {
        'uuid': user_info.organization_id.id,
        'uuid_hash': student_hash
      })
    )

    return context


