from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.models import Distribution,Organization,Classification
from submission_form.forms import CategoryForm


class CategoryIndexView(LoginRequiredMessageMixin, generic.ListView):
  """科目の一覧."""

  model = Classification
  template_name = 'submission_form/category_list.html'
  context_object_name='category_list'
  paginate_by = 20

  def get_queryset(self):
    """所属Orgの科目のみ抽出"""
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    try:
      if user_info is None:
        raise Classification.DoesNotExist
      return Classification.objects\
              .filter(organization_id = user_info.organization_id)\
              .order_by('-published_date')
    except Task.DoesNotExist:
      return None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context['is_teacher'] = StudentOrTeacherGetter.is_teacher(self.request.user)
    return context


class CategoryCreateView(LoginRequiredMessageMixin, generic.CreateView):
  """科目の作成."""

  model = Classification
  template_name = 'submission_form/category_form.html'
  form_class = CategoryForm
  success_url = reverse_lazy('submission_form:category_index')
    
  def get(self, request, **kwargs):
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    if not is_teacher:
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)

  def form_valid(self, form):
    category = form.save(commit = False)
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)

    category.user_id = self.request.user
    category.organization_id = user_info.organization_id
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
    user_info = StudentOrTeacherGetter.getInfo(request.user)
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    
    if not is_teacher or user_info.organization_id == get_object_or_404(Classification, id = kwargs['pk']).organization_id:
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
    user_info = StudentOrTeacherGetter.getInfo(request.user)
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    
    if not is_teacher or user_info.organization_id == get_object_or_404(Classification, id = kwargs['pk']).organization_id:
      raise Http404
    return super().get(request, **kwargs)

