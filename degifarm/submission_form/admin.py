from django.contrib import admin

from .models import Organization, Sex, Group, Classification, Student, Submission, Teacher, Distribution

# Register your models here.

admin.site.register(Organization)
admin.site.register(Sex)
admin.site.register(Group)
admin.site.register(Classification)
admin.site.register(Student)
admin.site.register(Submission)
admin.site.register(Teacher)
admin.site.register(Distribution)
