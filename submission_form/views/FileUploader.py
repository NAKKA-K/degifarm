# django module
from django.conf import settings

# app module

# lib


class FileUploader(Object):

  def __init__(self, files):
    self.files = files

  def handle_uploaded_files():
    for f in self.files:
      file = File(f)
      file.handle_uploaded_file()

  
  class File(Object):

    def __init__(self, file):
      self.file = file
      self.name = self.file.name
      self.path = '{}'.format(settings.MEDIA_ROOT) # TODO:後に課題ごとなどにディレクトリをまとめる可能性あり

    def handle_uploaded_file(self):
      make_dir()

      with open('{}{}'.format(self.path, self.name), 'wb+') as dest:
        for chunk in self.file.chunks():
          dest.write(chunk)

    def make_dir(self):
      if not os.path.exists(self.path):
        os.makedirs(self.path)

