# django module
from django.conf import settings

# app module

# lib
import mimetypes
import os


class FileUploader(object):
  """
  UploadFileオブジェクトのリストを受け取って、色々処理してくれるクラス。
  """
  def __init__(self, files, user = '__TMP__'):
    self.files = files
    self.files_path_list = []
    self.user = user
    self.files_dir = '{}{}'.format(settings.MEDIA_ROOT, user) # TODO:後に課題ごとなどにディレクトリをまとめる可能性あり

  def handle_uploaded_files(self):
    """
    FileUploaderに渡された複数ファイルをすべて保存する。
    保存ディレクトリが存在しない場合は、ディレクトリを作成する。
    """
    self.make_dir()
    for f in self.files:
      file = self.UploadFileHandler(f, self.files_dir)
      file.handle_uploaded_file()
      self.files_path_list.append(file.get_full_path())

  def make_dir(self):
    if not os.path.exists(self.files_dir):
      os.makedirs(self.files_dir)

  
  class UploadFileHandler(object):
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

