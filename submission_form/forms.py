from django import forms
from submission_form.models import Classification
from submission_form.views.StudentOrTeacherGetter import StudentOrTeacherGetter

class UploadFilesForm(forms.Form):
    classification = forms.ModelChoiceField(Classification.objects, label = '分野')
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}))

    def __init__(self, org_id = None, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['classification'].queryset = Classification.objects.filter(organization_id = org_id)

