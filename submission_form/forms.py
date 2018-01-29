from django import forms
from django.contrib.auth.forms import UserCreationForm

from submission_form.models import Classification, Organization, Teacher, User, Student
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

class UploadFilesForm(forms.Form):
    classification = forms.ModelChoiceField(Classification.objects, label = '分野')
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}))

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)

class OrganizationForm(forms.ModelForm):
  class Meta:
    model = Organization
    fields = ['name']

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name']

class TeacherForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = ['sex_id']

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['group_id', 'sex_id', 'school_year', 'school_class', 'school_number']

