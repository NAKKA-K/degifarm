# django module
from django.test import TestCase
from django.core.files.uploadedfile import UploadedFile
from django.core.files.base import File

# app module
from submission_form.views.FileUploader import FileUploader
from submission_form.models import User, Organization, Group, Sex, Student, Classification

# lib
import os
import io
from PIL import Image


class FileUploderClassTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(email = 'test@test.com',
                                         password = 'testpass1')
    org = Organization.objects.create(name = 'test org')
    group = Group.objects.create(organization_id = org,
                                 name = 'test group')
    sex = Sex.objects.create(name = '男性')
    Student.objects.create(user = self.user,
                           organization_id = org,
                           group_id = group,
                           sex_id = sex)
    self.classes = Classification.objects.create(organization_id = org,
                                                 name = 'test class')

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
    file_uploader = FileUploader(self.upload_file_instances, self.classes.id, self.user)
    file_uploader.handle_uploaded_files()
    
    # Exist files?
    for file_path in ['test.txt', 'test.png']:
      file_path = file_uploader.files_dir + file_path
      if os.path.exists(file_path):
        os.remove(file_path)
      else:
        self.fail('ファイルが保存されていません')

    import shutil
    shutil.rmtree(file_uploader.files_dir)
   

  def test_upload_page(self):
    client = self.client
    client.login(email = 'test@test.com', password = 'testpass1')

    self.assertEqual(client.get('/submission_form/upload/form/').status_code, 200)

    data = {
      'classification': self.classes.id,
      'files': self.upload_file_instances
    }
    
    response = client.post('/submission_form/upload/form/', data)
    self.assertEqual(response.status_code, 302)


