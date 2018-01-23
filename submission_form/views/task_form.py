# django module
from django.views.generic.base import TemplateView

# app module
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

# lib


# here views ============================================

class TaskHomeView(LoginRequiredMessageMixin, TemplateView):
  template_name = 'submission_form/task_home.html'


