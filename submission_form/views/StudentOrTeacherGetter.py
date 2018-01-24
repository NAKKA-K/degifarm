from submission_form.models import Student, Teacher

class StudentOrTeacherGetter(object):
  @classmethod
  def getInfo(cls, user):
    try:
      return Student.objects.get(user = user)
    except Student.DoesNotExist:
      try:
        return Teacher.objects.get(user = user)
      except Teacher.DoesNotExist:
        return None

  @classmethod
  def is_teacher(cls, user):
    try:
      Teacher.objects.get(user = user)
      return True
    except Teacher.DoesNotExist:
      try:
        Student.objects.get(user = user)
        return False
      except Student.DoesNotExist:
        return False



