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


