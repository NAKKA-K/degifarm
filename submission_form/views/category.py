from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.models import Distribution,Organization,Classification
from submission_form.forms import CategoryForm
import sweetify

#エラーページの読み込み
ERROR_404_TEMPLATE_NAME = '404.html'

class CategoryIndexView(LoginRequiredMessageMixin, generic.ListView):
  """科目の一覧."""

  model = Classification
  template_name = 'submission_form/category_list.html'
  context_object_name='category_list'
  queryset = Classification.objects.order_by('-published_date')
  paginate_by = 20


class CategoryCreateView(LoginRequiredMessageMixin, generic.CreateView):
  """科目の作成."""

  model = Classification
  template_name = 'submission_form/category_form.html'
  form_class = CategoryForm
  success_url = reverse_lazy('submission_form:category_index')
    
  def get(self, request, **kwargs):
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    if not is_teacher:
      template_name=ERROR_404_TEMPLATE_NAME
      sweetify.warning(self.request, title='ページがありません',confirmButtonColor='#dd6b55',button='OK')
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)

  def form_valid(self, form):
    category = form.save(commit = False)
    category.user_id = self.request.user
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
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
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    if not is_teacher:
      template_name=ERROR_404_TEMPLATE_NAME
      sweetify.warning(self.request, title='ページがありません',confirmButtonColor='#dd6b55',button='OK')
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)


class CategoryDeleteView(LoginRequiredMessageMixin, generic.DeleteView):
  """科目の削除."""

  model = Classification
  context_object_name='category'
  template_name = 'submission_form/category_confirm_delete.html'
  success_url = reverse_lazy('submission_form:category_index')

  def get(self, request, **kwargs):
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    if not is_teacher:
      template_name=ERROR_404_TEMPLATE_NAME
      sweetify.warning(self.request, title='ページがありません',confirmButtonColor='#dd6b55',button='OK')
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)


