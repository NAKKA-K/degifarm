import os
from django.db import models
from django.utils import timezone
from datetime import datetime

class Subject(models.Model):
  """科目"""
  name = models.CharField('科目名', max_length=255)
  create_at = models.DateTimeField('作成日', default=timezone.now)

  def __str__(self):
      return self.name

def get_upload_to(instance,filename):
  """upload_toを動的に指定"""
  try:
      path = os.path.join(str(instance.subject.name),filename)
  except:
      path = os.path.join('Nosubject',filename)
  return path


def default_subject():
  """デフォルトの科目を返す(まだなければ作る)"""
  subject, _ = Subject.objects.get_or_create(name='Nosubject')
  return subject



class File(models.Model):
  """アップロードする配布ファイル"""

  title = models.CharField('タイトル', max_length=255, blank=True)
  subject = models.ForeignKey(
      Subject, verbose_name='科目', on_delete=models.PROTECT,
      default=default_subject,
  )
  src = models.FileField('ファイル',upload_to=get_upload_to)
  create_at = models.DateTimeField('作成日', default=timezone.now)

  def __str__(self):
      return self.title

  def get_filename(self):
      """ファイル名を返す関数"""
      return os.path.basename(self.src.name)
