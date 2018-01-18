# django module
from django.test import TestCase

# app module
from submission_form.models import User

# lib



class LoginLogoutTest(TestCase):
  def setUp(self):
    self.user = User.objects.create_user(email = 'test@test.com', password = 'testpass1', first_name = 'first', last_name = 'last')
    

  def test_login(self):
    client = self.client

    # non login
    response = client.get('/')
    self.assertEqual(response.status_code, 200)

    response = client.get('/submission_form/')
    self.assertEqual(response.status_code, 302)

    # login
    client.login(email = 'test@test.com', password = 'testpass1')

    response = client.get('/')
    self.assertEqual(response.status_code, 200)

    response = client.get('/submission_form/')
    self.assertEqual(response.status_code, 200)

