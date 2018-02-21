# django module
from django.test import TestCase

# app module
from submission_form.models import User, Organization, Group, Sex, Student

# lib



class LoginLogoutTest(TestCase):
  def setUp(self):
    org = Organization.objects.create(name = 'test org')
    group = Group.objects.create(organization_id = org, name = 'test group')
    sex = Sex.objects.create(name = '男性')

    user = User.objects.create_user(email = 'test@test.com', password = 'testpass1')
    Student.objects.create(user = user, organization_id = org, group_id = group, sex_id = sex)

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

