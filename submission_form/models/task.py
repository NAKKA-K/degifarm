from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

from submission_form.models import Organization, Classification

class Task(models.Model):
  organization_id = models.ForeignKey(
    Organization,
    verbose_name = _('所属ID'),
    on_delete = models.CASCADE
  )
  user_id = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    verbose_name = _('課題提出者'),
    on_delete = models.CASCADE
  )
  classification_id = models.ForeignKey(
    Classification,
    verbose_name = _('科目'),
    on_delete = models.CASCADE
  )
  name = models.CharField(_('課題ファイル名'), max_length = 64)
  text = models.TextField(_('課題説明'))
  deadline = models.DateTimeField(_('提出期限'), help_text = 'xxxx-xx-xx の形式で入力してください')
  published_date = models.DateTimeField(_('公開日'), default = timezone.now, editable = False)

  def get_absolute_url(self, *args, **kwargs):
    return reverse('submission_form:task_detail', kwargs = {'pk':self.pk})
