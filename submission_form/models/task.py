from django.db import models
from django.utils import timezone
from django.conf import settings

from submission_form.models import Organization, Classification

class Task(models.Model):
  organization_id = models.ForeignKey(Organization)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
  classification_id = models.ForeignKey(Classification)
  name = models.CharField(max_length = 64)
  text = models.TextField()
  deadline = models.DateTimeField()
  published_date = models.DateTimeField(default = timezone.now, editable = False)
