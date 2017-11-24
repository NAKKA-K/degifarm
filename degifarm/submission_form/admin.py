from django.contrib import admin

from .models import Organization, Sex, Group, Classification, Student, Submission, Teacher, Distribution

# Register your models here.

class OrganizationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', )

class SexAdmin(admin.ModelAdmin):
  list_display = ('name', )

class GroupAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', )

class ClassificationAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', )

class StudentAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'group_id', 'name', 'email', 'sex_id', )

class SubmissionAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', 'student_id', 'published_date', )

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', 'email', )

class DistributionAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', 'teacher_id', 'published_date', )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Distribution, DistributionAdmin)
