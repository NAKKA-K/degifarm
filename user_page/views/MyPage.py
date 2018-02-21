from django.views.generic import TemplateView
from django.http import Http404

from submission_form.views import LoginRequiredMessageMixin
from submission_form.models import Student, Teacher, User


# Create your views here.
class MyPage(LoginRequiredMessageMixin, TemplateView):
    template_name = 'user_page/mypage.html'

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if request.session['is_teacher']:
            context['user_info'] = Teacher.objects.get(id = self.user)
        else:
            context['user_info'] = Student.objects.get(id = self.user)
        
        return context
    """


