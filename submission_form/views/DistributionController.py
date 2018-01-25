from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic

from .form import FileForm, SubjectForm
from .models import File, Subject

#pkはプライマリキー

class FileIndexView(generic.ListView):
      """ファイル一覧"""

      model = File
      queryset = File.objects.order_by('-create_at')
      paginate_by = 20

class FileSubjectView(generic.ListView):
      """科目別の配布ファイル一覧"""

      model = File
      paginate_by = 20

      def get_queryset(self):
          """科目ごとにフィルターかける"""
         subject_pk = self.kwargs['subject_pk']
         return File.objects.filter(
            subject__pk=subject_pk).order_by('-create_at')

      def get_context_data(self)
          """科目のpkをテンプレートへ渡す"""
         context = super(),get_context_data(*args, **kwargs) 
         context['subject_pk'] = self.kwargs.get('subject_pk')
         return context

class FileCreateView(generic.CreateView):
  """ファイルの作成"""
  model = File 
  form_class = FileForm
  success_url - reverse_lazy('forms:file_index')

  def get_initial(self):
      """科目の指定があれば、そのカテゴリを選択状態に"""
      initial = super().get_initial()
      initial['subject'] = self.kargs.get('subject_pk')
      return initial

class FileUpdateView(generic.UpdateView):
    """ファイルの更新."""

    model = File
    form_class = FileForm
    success_url = reverse_lazy('forms:file_index')


class FileDeleteView(generic.DeleteView):
    """ファイルの削除."""

    model = File
    success_url = reverse_lazy('forms:file_index')


class SubjectIndexView(generic.ListView):
    """科目の一覧."""

    model = Subject
    queryset = subject.objects.order_by('-created_at')
    paginate_by = 20


class SubjectCreateView(generic.CreateView):
    """科目の作成."""

    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy('forms:subject_index')


class SubjectUpdateView(generic.UpdateView):
    """科目名の更新."""

    model = Subject
    form_class = SubjectForm
    success_url = reverse_lazy('forms:subject_index')


class SubjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    """科目の削除."""

    model = Subject
    success_url = reverse_lazy('forms:subject_index')
