from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

# 団体テーブル
class Organization(models.Model):
  uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  name = models.CharField(max_length = 64)

# 性別マスタ
class Sex(models.Model):
  name = models.CharField(max_length = 4)

# 学科テーブル
class Group(models.Model):
  organization_id = models.ForeignKey(Organization, primary_key = True)
  id = models.IntegerField(primary_key = True)
  name = models.CharField(max_length = 64)

# 分類テーブル
class Classification(models.Model):
  organization_id = models.ForeignKey(Organization, primary_key = True)
  id = models.IntegerField(primary_key = True)
  name = models.CharField(max_length = 64)

# 学生テーブル
class Student(models.Model):
  organization_id = models.ForeignKey(Organization, primary_key = True)
  id = models.CharField(primary_key = True, max_length = 32)
  group_id = models.ForeignKey(Group)
  sex_id = models.ForeignKey(Sex)
  name = models.CharField(null = False, max_length = 64)
  # TODO: 学年、クラス、番号をどうするか？
  email = models.EmailField(null = False)

# 提出物テーブル
class Submission(models.Model):
  organization_id = models.ForeignKey(Organization, primary_key = True)
  student_id = models.ForeignKey(Student, primary_key = True)
  uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  classification_id = models.ForeignKey(Classification)
  name = models.CharField(max_length = 64)
  published_date = models.DateTimeField(null = False, default = timezone.now, editable = False)
  # TODO: 権限をどうするか？
  path = models.CharField(max_length = 128)






