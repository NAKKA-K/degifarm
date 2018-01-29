from django import forms
<<<<<<< HEAD
from submission_form.models import Classification,Distribution
=======
from django.contrib.auth.forms import UserCreationForm

from submission_form.models import Classification, Organization, Teacher, User
>>>>>>> 5b2b724191adde0879dab87f6153853c16057d84
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

class UploadFilesForm(forms.Form):
    classification = forms.ModelChoiceField(Classification.objects, label = '分野')
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}))

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)

<<<<<<< HEAD

class FileForm(forms.ModelForm):
    """Fileモデルのフォーム."""

    class Meta:
        model = Distribution
        fields = '__all__'
        widgets = {
            #'title': forms.TextInput(attrs={
            #    'class': "form-control",
            #}),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
          #  'classification_id': forms.Select(attrs={
          #      'class': "form-control",
          #  }),
            'published_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }

class CategoryForm(forms.ModelForm):
    """Subjectモデルのフォーム."""

    class Meta:
        model = Classification
        exclude = ('organization_id',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'published_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }
=======
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

>>>>>>> 5b2b724191adde0879dab87f6153853c16057d84

