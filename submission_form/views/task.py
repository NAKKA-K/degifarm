# django module
from django.views.generic.list import ListView

# app module
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.models import Task, Classification

# lib


# here views ============================================

class TaskHomeView(LoginRequiredMessageMixin, ListView):
  model = Task
  template_name = 'submission_form/task_home.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    try:
      if user_info is None:
        raise Task.DoesNotExist
      return Task.objects.filter(organization_id = user_info.organization_id)
    except Task.DoesNotExist:
      return None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    # userにリーレーションされるStudentかTeacherのレコードを取得する
    user_info = StudentOrTeacherGetter.getInfo(self.request.user)
    if user_info is not None:
      context['classification'] = Classification.objects.filter(organization_id = user_info.organization_id)
    return context




