from django import forms
from submission_form.models import Classification, File, Subject
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

class UploadFilesForm(forms.Form):
    classification = forms.ModelChoiceField(Classification.objects, label = '分野')
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}))

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)



class FileForm(forms.ModelForm):
    """Fileモデルのフォーム."""

    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
            'subject': forms.Select(attrs={
                'class': "form-control",
            }),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }



class SubjectForm(forms.ModelForm):
    """Subjectモデルのフォーム."""

    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'created_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
            }),
        }
