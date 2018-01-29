"""
# django module
from django.test import TestCase

# app module
from submission_form.models import User, Sex

# lib



class LoginLogoutTest(TestCase):
  def setUp(self):
    Sex.objects.create(name = '男性')

  def test_start_service(self):
    client = self.client

    response = client.get('/accounts/')
    self.assertEqual(response.status_code, 200)

    date = {
      'name': 'テスト学校',
      'email': 'test@test.com',
      'first_name': 'test',
      'last_name': 'com',
      'password1': 'testpass1',
      'password2': 'testpass1',
      'sex_id': 1,
    }
    
    response = client.post('/accounts/', date)
    self.assertEqual(response.status_code, 200)

    print(User.objects.all()) # Userが生成されていないので、フォームに成功していない
    client.login(email = 'test@test.com', password = 'testpass1')
    response = client.get('/submission_form/')
    self.assertEqual(response.status_code, 200)

"""
