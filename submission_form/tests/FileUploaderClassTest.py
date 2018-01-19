# django module
from django.test import TestCase
from django.core.files.uploadedfile import UploadedFile
from django.core.files.base import File

# app module
from submission_form.views.FileUploader import FileUploader

# lib
import os
import io
from PIL import Image


class FileUploderClassTest(TestCase):
  def setUp(self):
    # Generate test files
    self.upload_file_instances = []
    self.upload_file_instances.append(
        UploadedFile(file = File(self.generate_text_file()))
    )
    self.upload_file_instances.append(
      UploadedFile(file = File(self.generate_image_file()))
    )
    
  def generate_text_file(self):
    test_file = io.BytesIO(b'This is test file.')
    test_file.name = 'test.txt'
    test_file.content_type = 'text/plain'
    return test_file

  def generate_image_file(self):
    test_file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(test_file, 'png')
    test_file.name = 'test.png'
    test_file.seek(0)
    return test_file

  def test_file_uploder(self):
    # File upload
    file_uploader = FileUploader(self.upload_file_instances)
    file_uploader.handle_uploaded_files()
    
    # Exist files?
    for file_path in file_uploader.files_path_list:
      if os.path.exists(file_path):
        os.remove(file_path)
      else:
        self.fail('ファイルが保存されていません')

  #def test_upload_page(self):
    
