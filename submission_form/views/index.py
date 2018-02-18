from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'submission_form/index.html'

