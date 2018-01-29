
from django.db import models
from django.utils import timezone
from django.conf import settings

# app module

# lib
import uuid


# Create your models here.

# 団体テーブル
class Organization(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

# 性別マスタ
class Sex(models.Model):
  CHOICES = (('男性', '男性'),('女性', '女性'),('その他', 'その他'),)

  name = models.CharField(max_length = 4, choices = CHOICES)

  def __str__(self):
    return self.name

# 学科テーブル
class Group(models.Model):
  organization_id = models.ForeignKey(Organization)
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

# 分類テーブル
class Classification(models.Model):
  organization_id = models.ForeignKey(Organization)
  name = models.CharField('カテゴリ名',max_length = 64)
  published_date = models.DateTimeField('作成日', default=timezone.now)


  def __str__(self):
    return self.name


# 提出物テーブル
class Submission(models.Model):
  organization_id = models.ForeignKey(Organization)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification)
  name = models.CharField(max_length = 64)
  published_date = models.DateTimeField('作成日', default=timezone.now)
  path = models.CharField(max_length = 255)

  def __str__(self):
    return self.name


# 配布物テーブル
class Distribution(models.Model):
  organization_id = models.ForeignKey(Organization)
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(
  Classification,
  verbose_name='カテゴリ',
  )
  name = models.CharField(max_length = 64)
  published_date = models.DateTimeField('作成日', default=timezone.now)
  path = models.CharField(max_length = 255)

  def __str__(self):
    return self.name



