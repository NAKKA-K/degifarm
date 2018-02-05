from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.conf import settings

# app module

# lib
import uuid


# Create your models here.

# 団体テーブル
class Organization(models.Model):
  id = models.UUIDField(_('所属ID'), primary_key = True, default = uuid.uuid4, editable = False)
  name = models.CharField(_('所属'), max_length = 64)

  def __str__(self):
    return self.name


# 性別マスタ
class Sex(models.Model):
  CHOICES = (('男性', '男性'),('女性', '女性'),('その他', 'その他'),)

  name = models.CharField(_('性別'), max_length = 4, choices = CHOICES)

  def __str__(self):
    return self.name


# 学科テーブル
class Group(models.Model):
  organization_id = models.ForeignKey(Organization, verbose_name = _('所属ID'))
  name = models.CharField(_('学科'), max_length = 64)

  def __str__(self):
    return self.name


# 分類テーブル
class Classification(models.Model):
  organization_id = models.ForeignKey(Organization, verbose_name = _('所属ID'))
  name = models.CharField(_('科目名'), max_length = 64)
  published_date = models.DateTimeField(_('作成日'), default=timezone.now)

  def __str__(self):
    return self.name


# 提出物テーブル
class Submission(models.Model):
  organization_id = models.ForeignKey(Organization, verbose_name = _('所属ID'))
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = _('提出者'))
  id = models.UUIDField(_('提出ID'), primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification, verbose_name = _('科目'))
  name = models.CharField(_('ファイル名'), max_length = 64)
  published_date = models.DateTimeField(_('公開日'), default=timezone.now)
  path = models.CharField(_('ファイルパス'), max_length = 255)

  def __str__(self):
    return self.name


# 配布物テーブル
class Distribution(models.Model):
  organization_id = models.ForeignKey(Organization, verbose_name = _('所属ID'))
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = _('配布者'))
  id = models.UUIDField(_('配布ID'), primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification, verbose_name = _('科目'))
  name = models.CharField(_('ファイル名', ), max_length = 64)
  published_date = models.DateTimeField(_('公開日'), default=timezone.now)
  path = models.CharField(_('ファイルパス'), max_length = 255)

  def __str__(self):
    return self.name

