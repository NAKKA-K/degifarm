# django module
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils import timezone
from django.http import Http404

# app module
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.models import Organization, Task, Classification, Teacher, Submission

# lib


# here views ============================================

class TaskHomeView(LoginRequiredMessageMixin, ListView):
  model = Task
  template_name = 'submission_form/task_home.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    try:
      return Task.objects\
             .filter(organization_id = self.request.session['user_info']['org'])\
             .filter(published_date__lte = timezone.now())
    except Task.DoesNotExist:
      return None

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['classification'] = Classification.objects\
                                .filter(organization_id =\
                                    self.request.session['user_info']['org'])

    """ # TODO:
    現状、submissionの取得。taskの取得。その後2つのリストを2重ループで比較という処理になっている。
    同じことをSQL文でleft joinすれば簡単に処理できる。
    しかし、djangoのqueryの仕様上、どう書けばよいのか不明だったため後回しとする。
    """
    # データ量削減のためにnameだけを取得し、userだけに絞る
    submission = Submission.objects.filter(user_id = self.request.user)

    status_list = []
    for task in context['task_list']:
      if not submission:
        status_list.append('未')
        next

      for sub in submission:
        if task.classification_id == sub.classification_id and task.name == sub.name:
          status_list.append('済')
          break
      else:
        status_list.append('未')
    else:
      context['status_list'] = status_list

    return context


class TaskCreateView(LoginRequiredMessageMixin, CreateView):
  model = Task
  fields = ['classification_id', 'name', 'text', 'deadline']
  template_name = 'submission_form/task_create.html'

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404 # 先生でなければ、PageNotFound
    return super().get(request, **kwargs)

  def form_valid(self, form):
    task = form.save(commit = False)
    task.user_id = self.request.user
    task.organization_id = \
        Organization.objects\
        .get(id = self.request.session['user_info']['org'])
    task.save()
    return super().form_valid(form)


class TaskDetailView(LoginRequiredMessageMixin, DetailView):
  model = Task
  template_name = 'submission_form/task_detail.html' 


class TaskEditView(LoginRequiredMessageMixin, UpdateView):
  model = Task
  fields = ['classification_id', 'name', 'text', 'deadline']
  template_name = 'submission_form/task_edit.html'

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)


class TaskDeleteView(LoginRequiredMessageMixin, DeleteView):
  model = Task
  template_name = 'submission_form/task_detail.html'
  success_url = reverse_lazy('submission_form:index')

  def get(self, request, **kwargs):
    if not request.session['is_teacher']:
      raise Http404
    return super().get(request, **kwargs)

