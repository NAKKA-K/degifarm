# django module
from django.views.generic.list import ListView
from django.utils import timezone

# app module
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.models import Task, Classification, Teacher, Submission

# lib
from datetime import timedelta


# here views====================================

class HomeView(LoginRequiredMessageMixin, ListView):
    model = Task
    template_name = 'submission_form/home.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        user_info = StudentOrTeacherGetter.getInfo(self.request.user)
        try:
            if user_info is None:
                raise Task.DoesNotExist
            # 提出期限が1週間後までの課題のみ取得
            return Task.objects.filter(organization_id = user_info.organization_id).filter(published_date__lte = timezone.now(), deadline__gte = timezone.now(), deadline__lte = timezone.now() + timedelta(days = 7))
        except Task.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # userにリーレーションされるStudentかTeacherのレコードを取得する
        user_info = StudentOrTeacherGetter.getInfo(self.request.user)
        if user_info is None:
            return context

        context['classification'] = Classification.objects.filter(organization_id = user_info.organization_id)
        context['is_teacher'] = StudentOrTeacherGetter.is_teacher(self.request.user)

        if not context['task_list']: # 1週間以内の課題がない場合に、Submissionを取得すると処理の無駄になるため
            return context

        # TODO: 現状、submissionの取得。taskの取得。その後2つのリストを2重ループで比較という処理になっている。
        # 同じことをSQL文でleft joinすれば簡単に処理できる。
        # しかし、djangoのqueryの仕様上、どう書けばよいのか不明だったため後回しとする。

        # データ量削減のためにnameだけを取得し、userだけに絞る
        submission = Submission.objects.filter(user_id = self.request.user)

        status_list = []
        for task in context['task_list']:
            if not submission: # submissionの中身が存在しない場合のため(中で書く理由はtask_listの長さだけstatus_listが必要なため)
                status_list.append('未')
                next

            for sub in submission:
                if task.classification_id == sub.classification_id and task.name == sub.name:
                    status_list.append('済')
                    break
                else:
                    status_list.append('未')
                    break
        else:
            context['status_list'] = status_list

        return context

