from django.test import TestCase

from submission_form.models import User

class SiteGetTest(TestCase):
  def setUp(self):
    User.objects.create_user(email = 'test@test.com', password = 'testpass1')

  def test_get_all_page(self):
    client = self.client

    # non logined
    self.assertEqual(client.get('/').status_code, 200)
    self.assertEqual(client.get('/accounts/').status_code, 200)
    self.assertEqual(client.get('/accounts/login/').status_code, 200)
    self.assertEqual(client.get('/accounts/logout/').status_code, 302)
    self.assertEqual(client.get('/submission_form/').status_code, 302)
    self.assertEqual(client.get('/submission_form/upload/').status_code, 302)
    self.assertEqual(client.get('/submission_form/upload/form/').status_code, 302)



    # login
    client.login(email = 'test@test.com', password = 'testpass1')

    self.assertEqual(client.get('/').status_code, 200)
    self.assertEqual(client.get('/accounts/').status_code, 200)
    self.assertEqual(client.get('/accounts/login/').status_code, 200)
    self.assertEqual(client.get('/submission_form/').status_code, 200)
    self.assertEqual(client.get('/submission_form/upload/').status_code, 200)
    self.assertEqual(client.get('/submission_form/upload/form/').status_code, 200)

    self.assertEqual(client.get('/accounts/logout/').status_code, 302)
