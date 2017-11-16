from django import forms

class UploadFilesForm(forms.Form):
    files = forms.FileField(widget = forms.ClearableFileInput(attrs = {'multiple': True}))
