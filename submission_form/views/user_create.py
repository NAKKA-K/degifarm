from django.views.generic.base import TemplateView, View
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import transaction

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.models import Organization
from submission_form.forms import CustomUserCreationForm, TeacherForm, StudentForm

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

    # ユーザー作成ViewのURLを作成
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


class UserCreateView(View):
  template_name = 'user_create.html'
  success_url = reverse_lazy('index')

  def get(self, request, **kwargs):
    if self.is_teacher_create(self.kwargs['uuid'], self.kwargs['uuid_hash']):
      data = {
        'user_form': CustomUserCreationForm(),
        'user_info_form': TeacherForm(),
      }
    else:
      data = {
        'user_form': CustomUserCreationForm(),
        'user_info_form': StudentForm(),
      }
    return render(request, self.template_name, data)

  @transaction.atomic
  def post(self, request, **kwargs):
    if self.is_teacher_create(self.kwargs['uuid'], self.kwargs['uuid_hash']):
      user_form = CustomUserCreationForm(request.POST)
      user_info_form = StudentForm(request.POST)
    else:
      user_form = CustomUserCreationForm(request.POST)
      user_info_form = TeacherForm(request.POST)

    if user_form.is_valid() and user_info_form.is_valid():
      user = user_form.save()

      user_info = user_info_form.save(commit = False)
      user_info.user = user
      user_info.organization_id = Organization.objects.get(id = self.kwargs['uuid'])
      user_info.save()

      messages.success(request, 'アカウントが作成されました。ようこそ、でじふぁーむ。へ')
      return redirect('index')

    data = {
      'user_form': user_form,
      'user_info_form': user_info_form,
    }
    messages.error(request, 'データに不備があります')
    return render(request, self.template_name, data)

  def is_teacher_create(self, uuid, uuid_hash):
    if not Organization.objects.get(id = uuid):
      raise Http404

    # sha224はある程度重い処理なので、検査を分割することで少しばかりの処理速度軽減
    teacher_hash = hashlib.sha224(str(uuid).encode('utf-8'))
    teacher_hash.update('teacher'.encode('utf-8'))
    if teacher_hash.hexdigest() == uuid_hash:
      return True

    student_hash = hashlib.sha224(str(uuid).encode('utf-8'))
    student_hash.update('student'.encode('utf-8'))
    if student_hash.hexdigest() == uuid_hash:
      return False
    else:
      raise Http404


