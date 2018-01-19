# django module
from django.test import TestCase

# app module
from submission_form.models import User

# lib



class LoginLogoutTest(TestCase):
  def setUp(self):
    User.objects.create_user(email = 'test@test.com', password = 'testpass1')

  def test_login(self):
    client = self.client

    # non logined
    response = client.get('/')
    self.assertEqual(response.status_code, 200)

    response = client.get('/submission_form/')
    self.assertEqual(response.status_code, 302)

    # logined
    client.login(email = 'test@test.com', password = 'testpass1')

    response = client.get('/')
    self.assertEqual(response.status_code, 200)

    response = client.get('/submission_form/')
    self.assertEqual(response.status_code, 200)

