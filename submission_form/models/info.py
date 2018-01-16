from django.db import models
from django.utils import timezone
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
  name = models.CharField(max_length = 4)

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
  name = models.CharField(max_length = 64)

  def __str__(self):
    return self.name

# 学生テーブル
class Student(models.Model):
  organization_id = models.ForeignKey(Organization)
  group_id = models.ForeignKey(Group)
  sex_id = models.ForeignKey(Sex)
  name = models.CharField(max_length = 64)
  # TODO: 学年、クラス、番号をどうするか？
  email = models.EmailField()

  def __str__(self):
    return self.name

# 提出物テーブル
class Submission(models.Model):
  organization_id = models.ForeignKey(Organization)
  student_id = models.ForeignKey(Student)
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification)
  name = models.CharField(max_length = 64)
  published_date = models.DateTimeField(default = timezone.now(), editable = False)
  path = models.CharField(max_length = 255)
  # TODO: 権限をどうするか？

  def __str__(self):
    return self.name


# 先生テーブル
class Teacher(models.Model):
  organization_id = models.ForeignKey(Organization)
  name = models.CharField(max_length = 64)
  email = models.EmailField()

  def __str__(self):
    return self.name

# 配布物テーブル
class Distribution(models.Model):
  organization_id = models.ForeignKey(Organization)
  teacher_id = models.ForeignKey(Teacher)
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification)
  name = models.CharField(max_length = 64)
  published_date = models.DateTimeField(default = timezone.now(), editable = False)
  path = models.CharField(max_length = 255)
  # TODO: 権限をどうするか？

  def __str__(self):
    return self.name


