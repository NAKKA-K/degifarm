from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from submission_form.models import Classification, Organization, Teacher, User, Student, Distribution, Group
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

class UploadFilesForm(forms.Form):
    classification = forms.ModelChoiceField(Classification.objects, label = '分野')
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}), label = 'ファイル(複数)')

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)


class FileForm(forms.Form):
    """Fileモデルのフォーム."""

    classification = forms.ModelChoiceField(Classification.objects, label = 'カテゴリ')
    file = forms.FileField(label = 'ファイル')

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)


class CategoryForm(forms.ModelForm):
  class Meta:
    model = Classification
    exclude = ('organization_id','published_date')
    widgets = {
        'name': forms.TextInput(attrs={
            'class': "form-control",
        }),
    }

class GroupForm(forms.ModelForm):
  class Meta:
    model = Group
    exclude = ('organization_id', )
    widgets = {
        'name': forms.TextInput(attrs={
            'class': "form-control",
        }),
    }


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
    labels = {
      'sex_id': _('性別')
    }

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['group_id', 'sex_id', 'school_year', 'school_class', 'school_number']
    labels = {
      'group_id': _('学科'),
      'sex_id': _('性別'),
      'school_year': _('学年'),
      'school_class': _('組'),
      'school_number': _('番号'),
    }

