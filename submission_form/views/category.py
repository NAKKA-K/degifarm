from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404

from submission_form.views import LoginRequiredMessageMixin
from submission_form.models import Distribution, Organization, Classification
from submission_form.forms import CategoryForm


class CategoryIndexView(LoginRequiredMessageMixin, generic.ListView):
  """科目の一覧."""

  model = Classification
  template_name = 'submission_form/category_list.html'
  context_object_name='category_list'
  paginate_by = 20

  def get_queryset(self):
    """所属Orgの科目のみ抽出"""
    try:
      return Classification.objects\
             .filter(organization_id = self.request.session['user_info']['org'])\
             .order_by('-published_date')
    except Classification.DoesNotExist:
      return None


class CategoryCreateView(LoginRequiredMessageMixin, generic.CreateView):
  """科目の作成."""

  model = Classification
  template_name = 'submission_form/category_form.html'
  form_class = CategoryForm
  success_url = reverse_lazy('submission_form:category_index')
    
  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)

  def form_valid(self, form):
    category = form.save(commit = False)

    category.user_id = self.request.session['user_info']['user']
    category.organization_id = \
        Organization.objects\
        .get(id = self.request.session['user_info']['org'])
    category.save()
    return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMessageMixin, generic.UpdateView):
  """科目名の更新."""

  model = Classification
  template_name = 'submission_form/category_form.html'
  form_class = CategoryForm
  success_url = reverse_lazy('submission_form:category_index')

  def get(self, request, **kwargs):
    """先生、所属Orgの科目以外なら404を返す"""
    if not request.session['is_teacher']\
       or request.session['user_info']['org'] != str(\
           get_object_or_404(Classification, id = kwargs['pk'])\
           .organization_id.id):
      raise Http404
    return super().get(request, **kwargs)


class CategoryDeleteView(LoginRequiredMessageMixin, generic.DeleteView):
  """科目の削除."""

  model = Classification
  context_object_name='category'
  template_name = 'submission_form/category_confirm_delete.html'
  success_url = reverse_lazy('submission_form:category_index')

  def get(self, request, **kwargs):
    """先生、所属Orgの科目以外なら404を返す"""
    
    if not request.session['is_teacher']\
       or request.session['user_info']['org'] != str(\
           get_object_or_404(Classification, id = kwargs['pk'])\
           .organization_id.id):
      raise Http404
    return super().get(request, **kwargs)

