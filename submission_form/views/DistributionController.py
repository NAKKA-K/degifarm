#django module
from django.urls import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.utils import timezone
from django.http import Http404

#app module
from submission_form.models import Distribution,Organization,Classification
from submission_form.forms import FileForm,CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter
from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

#
class FileIndexView(LoginRequiredMessageMixin,generic.ListView):
      """ファイル一覧"""

      model = Distribution
      template_name = 'submission_form/dist_list.html'
      context_object_name='file_list'
      queryset = Distribution.objects.order_by('-published_date')
      paginate_by = 20


class FileCategoryView(generic.ListView):
      """カテゴリ別の配布ファイル一覧"""

      model = Distribution
      paginate_by = 20

      def get_queryset(self):
          """カテゴリ(分類)ごとにフィルターかける"""
          category_pk = self.kwargs['category_pk']
          return Distribution.objects.filter(
            category__pk=category_pk).order_by('-published_date')

      def get_context_data(self):
          """カテゴリのpkをテンプレートへ渡す"""
          context = super().get_context_data(*args, **kwargs) 
          context['category_pk'] = self.kwargs.get('category_pk')
          return context


class FileCreateView(LoginRequiredMessageMixin,generic.CreateView):
      """ファイルの作成"""
      model = Distribution
      template_name = 'submission_form/dist_form.html'
      form_class = FileForm
      success_url = reverse_lazy('submission_form:dist_index')

      '''
      def get_initial(self):
          """科目の指定があれば、そのカテゴリを選択状態に"""
          initial = super().get_initial()
          initial['classification_id'] = self.kargs.get('dist_pk')
          return initial
      '''

class FileUpdateView(generic.UpdateView):
    """ファイルの更新."""

    model = Distribution
    template_name = 'submission_form/dist_form.html'
    form_class = FileForm
    success_url = reverse_lazy('submission_form:file_index')


class FileDeleteView(generic.DeleteView):
    """ファイルの削除."""

    model = Distribution
    context_object_name='file'
    template_name = 'submission_form/dist_confirm_delete.html'
    success_url = reverse_lazy('submission_form:file_index')


class CategoryIndexView(LoginRequiredMessageMixin,generic.ListView):
    """科目の一覧."""

    model = Classification
    template_name = 'submission_form/category_list.html'
    context_object_name='category_list'
    queryset = Classification.objects.order_by('-published_date')
    paginate_by = 20


class CategoryCreateView(LoginRequiredMessageMixin,generic.CreateView):
    """科目の作成."""

    model = Classification
    template_name = 'submission_form/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('submission_form:category_index')
      
    def form_valid(self, form):
      category = form.save(commit = False)
      category.user_id = self.request.user
      user_info = StudentOrTeacherGetter.getInfo(self.request.user)
      category.organization_id = user_info.organization_id
      category.save()
      return super().form_valid(form)
    
    

class CategoryUpdateView(generic.UpdateView):
    """科目名の更新."""

    model = Classification
    template_name = 'submission_form/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('submission_form:category_index')

class CategoryDeleteView(generic.DeleteView):
    """科目の削除."""

    model = Classification
    context_object_name='category'
    template_name = 'submission_form/category_confirm_delete.html'
    success_url = reverse_lazy('submission_form:category_index')
