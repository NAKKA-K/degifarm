#django module
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic.edit import FormView
from django.http import Http404
from django.conf import settings
import sweetify

#app module
from submission_form.models import Distribution, Organization, Classification
from submission_form.forms import FileForm
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

import os


class DistListView(LoginRequiredMessageMixin, generic.ListView):
  """配布物一覧"""

  model = Distribution
  template_name = 'submission_form/dist_list.html'
  context_object_name='file_list'
  queryset = Distribution.objects.order_by('-published_date')
  paginate_by = 20

  def get_context_data(self, **kwargs):
    """科目のpkをテンプレートへ渡す"""
    context = super().get_context_data(**kwargs) 
    context['class_list'] = \
        Classification.objects\
        .filter(organization_id = self.request.session['user_info']['org'])

    return context


class DistClassListView(LoginRequiredMessageMixin, generic.ListView):
  """科目別の配布物一覧"""

  model = Distribution
  context_object_name='file_list'
  paginate_by = 20
  template_name = 'submission_form/dist_list.html'

  def get_queryset(self):
    """科目ごとにフィルターかける"""
    category_pk = self.kwargs['category_pk']
    return Distribution.objects\
           .filter(classification_id = category_pk)\
           .order_by('-published_date')

  def get_context_data(self, **kwargs):
    """科目のpkをテンプレートへ渡す"""
    context = super().get_context_data(**kwargs) 
    context['category_pk'] = self.kwargs.get('category_pk')
    context['class_list'] = \
        Classification.objects\
        .filter(organization_id = self.request.session['user_info']['org'])

    return context


class DistUploadView(LoginRequiredMessageMixin, FormView):
  """配布物のアップロードフォーム"""

  template_name = 'submission_form/dist_form.html'
  form_class = FileForm
  success_url = reverse_lazy('submission_form:dist_index')

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)

  def get_form(self, form_class = None):
    return FileForm(org_id = self.request.session['user_info']['org']) 

  def post(self, request, *args, **kwargs):
    form = FileForm(request.POST)

    file = request.FILES['file']
    class_id = request.POST.get('classification', None)
    if not bool(form.errors):
      file_dir = '{}{}/'.format(settings.MEDIA_ROOT, request.user)
      self.make_dir(file_dir)
      file_path = '{}{}'.format(file_dir, file.name)

      with open(file_path, 'wb+') as dest:
        for chunk in file.chunks():
          dest.write(chunk)

      org = Organization.objects\
            .get(id = self.request.session['user_info']['org'])

      res = Distribution.objects.create(
        organization_id = org,
        user_id = request.user,
        classification_id = get_object_or_404(Classification, id = class_id),
        name = file.name,
        path = file_path,
      )
      return self.form_valid(form)
    else:
      return self.form_invalid(form)

  def make_dir(self, file_dir):
    if not os.path.exists(file_dir):
      os.makedirs(file_dir)


class DistUpdateView(LoginRequiredMessageMixin, generic.UpdateView):
  """配布物の更新"""

  model = Distribution
  template_name = 'submission_form/dist_form.html'
  form_class = FileForm
  success_url = reverse_lazy('submission_form:dist_index')

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)


class DistDeleteView(LoginRequiredMessageMixin, generic.DeleteView):
  """配布物の削除"""

  model = Distribution
  context_object_name = 'file'
  template_name = 'submission_form/dist_confirm_delete.html'
  success_url = reverse_lazy('submission_form:dist_index')

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)

  def post(self, request, **kwargs):
    dist = Distribution.objects.get(id = kwargs.get('pk'))
    try:
      os.remove(dist.path)
    except:
      pass

    return super().post(request, **kwargs)


