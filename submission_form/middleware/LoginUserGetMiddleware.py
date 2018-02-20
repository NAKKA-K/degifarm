from submission_form.views import StudentOrTeacherGetter
from django.forms.models import model_to_dict
from submission_form.models import Task

class LoginUserGetMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)  # action view!
        """
        if request.session['user_info'] is None:
            return response

        print(Task.objects.filter(
              organization_id = request.session['user_info']['org'],
              user_id = request.session['user_info']['user']))
        """
        
        return response

    def process_request(self, request):
        if request.user.is_anonymous:
            return

        user_info = StudentOrTeacherGetter.getInfo(request.user)
        is_teacher = StudentOrTeacherGetter.is_teacher(request.user)

        # UUID and Model not serialize
        user_info_dict = {
            'user': user_info.user.id,
            'org': str(user_info.organization_id.id)
        }

        request.session['user_info'] = user_info_dict
        request.session['is_teacher'] = is_teacher

