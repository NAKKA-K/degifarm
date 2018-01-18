# django module
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _

# app module
from .models import Organization, Sex, Group, Classification, Student, Submission, Teacher, Distribution
from .models import User

# lib

# Register your models here.
class MyUserChangesForm(UserChangeForm):
  class Meta:
    model = User
    fields = '__all__'

class MyUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('email',)

class MyUserAdmin(UserAdmin):
  fieldsets = (
      (None, {'fields': ('email', 'password')}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions' )}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  form = MyUserChangesForm
  add_form = MyUserCreationForm
  list_display = ('email', 'first_name', 'last_name', 'is_staff')
  list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email',)

admin.site.register(User, MyUserAdmin)


class OrganizationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', )

class SexAdmin(admin.ModelAdmin):
  list_display = ('name', )

class GroupAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', )

class ClassificationAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'name', )

class StudentAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'group_id', 'sex_id', )

class SubmissionAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'user_id', 'path', 'published_date', )

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'sex_id')

class DistributionAdmin(admin.ModelAdmin):
  list_display = ('organization_id', 'user_id', 'path', 'published_date', )


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Sex, SexAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Distribution, DistributionAdmin)

