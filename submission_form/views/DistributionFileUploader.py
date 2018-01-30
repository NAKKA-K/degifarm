# django module
from django.conf import settings
from django.shortcuts import get_object_or_404

# app module
from submission_form.models import Organization, Classification, Student, Teacher, Distribution

# lib
import mimetypes
import os


class DistributionFileUploader(object):
  """
  UploadFileオブジェクトのリストを受け取って、色々処理してくれるクラス。
  """
  def __init__(self, files, class_id, user = '__TMP__'):
    self.files = files
    self.user = user
    self.files_dir = '{}{}/'.format(settings.MEDIA_ROOT, user) # TODO:後に課題ごとなどにディレクトリをまとめる可能性あり
    self.class_id = class_id
    self.set_user_info()


  def handle_uploaded_files(self):
    """
    FileUploaderに渡された複数ファイルをすべて保存する。
    保存ディレクトリが存在しない場合は、ディレクトリを作成する。
    """
    self.make_dir()
    for f in self.files:
      file = self.DistributionFileHandler(f, self.files_dir)
      file.handle_uploaded_file()
      file.add_object_to_model(self.org_id, self.user, self.class_id)

  def make_dir(self):
    if not os.path.exists(self.files_dir):
      os.makedirs(self.files_dir)

  def set_user_info(self):
    # userの追加情報を取得(生徒か先生かわからないため、両方で取得を試みる)
    try:
      user_info = Student.objects.get(user = self.user)
    except Student.DoesNotExist:
      try:
        user_info = Teacher.objects.get(user = self.user)
      except Teacher.DoesNotExist:
        user_info = None

    self.org_id = user_info.organization_id

  
  class DistributionFileHandler(object):
    """
    UploadFileクラスを受け取って、ファイルとして保存するクラス。
    """

    def __init__(self, file, save_dir):
      self.file = file
      self.save_dir = save_dir

    def handle_uploaded_file(self):
      """
      インスタンス生成時に渡されたUploadFileオブジェクトを、
      外部クラスのFileUploaderのfiles_dirパス以下に保存する。
      """
      with open(self.get_full_path(), 'wb+') as dest:
        for chunk in self.file.chunks():
          dest.write(chunk)

    def get_full_path(self):
      return '{}{}'.format(self.save_dir, self.file.name)
      
    def get_mime_types(self):
      return mimetypes.guess_type(self.get_full_path())

    def add_object_to_model(self, org_id, user, class_id):
      Distribution.objects.create(
        organization_id = get_object_or_404(Organization, pk = org_id.id),
        user_id = user,
        classification_id = get_object_or_404(Classification, pk = class_id),
        name = self.file.name,
        path = self.get_full_path()
      )

