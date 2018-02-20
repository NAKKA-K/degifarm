from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import get_object_or_404

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.models import Group
from submission_form.forms import GroupForm


class GroupIndexView(LoginRequiredMessageMixin, generic.ListView):
  """科目の一覧."""

  model = Group
  template_name = 'submission_form/group_list.html'
  context_object_name='group_list'
  paginate_by = 20

  def get_queryset(self):
    """所属Orgの科目のみ抽出"""
    try:
      if self.request.session['user_info']['org'] is None:
        raise Group.DoesNotExist
      return Group.objects\
             .filter(organization_id = self.request.session['user_info']['org'])
    except Group.DoesNotExist:
      return None


class GroupCreateView(LoginRequiredMessageMixin, generic.CreateView):
  """科目の作成."""

  model = Group
  template_name = 'submission_form/group_form.html'
  form_class = GroupForm
  success_url = reverse_lazy('submission_form:group_index')
    
  def get(self, request, **kwargs):
    is_teacher = StudentOrTeacherGetter.is_teacher(request.user)
    if not is_teacher:
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)

  def form_valid(self, form):
    group = form.save(commit = False)

    group.organization_id = \
        Organization.objects\
        .get(id = self.request.session['user_info']['org'])
    group.save()
    return super().form_valid(form)


class GroupUpdateView(LoginRequiredMessageMixin, generic.UpdateView):
  """科目名の更新."""

  model = Group
  template_name = 'submission_form/group_form.html'
  form_class = GroupForm
  success_url = reverse_lazy('submission_form:group_index')

  def get(self, request, **kwargs):
    """先生、所属Orgの科目以外なら404を返す"""
    user_info = StudentOrTeacherGetter.getInfo(request.user)
    
    if not request.session['is_teacher']\
       or request.session['user_info']['org'] != str(\
           get_object_or_404(Group, id = kwargs['pk'])\
           .organization_id.id):
      raise Http404
    return super().get(request, **kwargs)


class GroupDeleteView(LoginRequiredMessageMixin, generic.DeleteView):
  """科目の削除."""

  model = Group
  context_object_name='group'
  template_name = 'submission_form/group_confirm_delete.html'
  success_url = reverse_lazy('submission_form:group_index')

  def get(self, request, **kwargs):
    """先生、所属Orgの科目以外なら404を返す"""
    
    if not request.session['is_teacher']\
       or request.session['user_info']['org'] != str(\
           get_object_or_404(Group, id = kwargs['pk'])\
           .organization_id.id):
      raise Http404
    return super().get(request, **kwargs)

