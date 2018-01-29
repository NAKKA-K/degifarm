from django.test import TestCase

from submission_form.models import User, Organization, Group, Sex, Student, Teacher

class SiteGetTest(TestCase):
  def setUp(self):
    org = Organization.objects.create(name = 'test org')
    group = Group.objects.create(organization_id = org, name = 'test group')
    sex = Sex.objects.create(name = '男性')

    student_user = User.objects.create_user(email = 'test@test.com', password = 'testpass1')
    Student.objects.create(user = student_user, organization_id = org, group_id = group, sex_id = sex)

    teacher_user = User.objects.create_user(email = 'test@test.teacher', password = 'testpass1')
    Teacher.objects.create(user = teacher_user, organization_id = org, sex_id = sex)
    

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


  def test_account_create_page(self):
    client = self.client

    self.assertEqual(client.get('/accounts/create/').status_code, 404)

    # 生徒は入れない
    client.login(email = 'test@test.com', password = 'testpass1')
    self.assertEqual(client.get('/accounts/create/').status_code, 404)

    # 先生は入れる
    client.login(email = 'test@test.teacher', password = 'testpass1')
    self.assertEqual(client.get('/accounts/create/').status_code, 200)


