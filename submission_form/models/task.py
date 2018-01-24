from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

from submission_form.models import Organization, Classification

class Task(models.Model):
  organization_id = models.ForeignKey(Organization)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
  classification_id = models.ForeignKey(Classification, verbose_name = '科目')
  name = models.CharField(max_length = 64, verbose_name = '提出ファイル名')
  text = models.TextField(verbose_name = '説明')
  deadline = models.DateTimeField(verbose_name = '提出期限', help_text = 'xxxx-xx-xx の形式で入力してください')
  published_date = models.DateTimeField(default = timezone.now, editable = False)

  def get_absolute_url(self, *args, **kwargs):
    return reverse('submission_form:task_detail', kwargs = {'pk':self.pk})
