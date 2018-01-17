from django.db import models
from django.utils import timezone

from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _

from django.conf import settings

class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    """
    Create and save a User with the given email, and password.
    """
    if not email:
      raise ValueError('The given email must be set')

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password = None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_supperuser=True')

    return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(
    _('email address'),
    unique = True,
    error_messages = {'unique': _("A user with that email already exists.")},
  )
  first_name = models.CharField(_('first name'), max_length = 30)
  last_name = models.CharField(_('last name'), max_length = 150)

  is_staff = models.BooleanField(
    _('staff status'),
    default = False,
    help_text = _('Designates whether the user can log into this admin site.')
  )
  is_active = models.BooleanField(
    _('active'),
    default = True,
    help_text = _(
      'Designates whether this user should be treated as active.'
      'Unselect this instead of deleting accounts.'
      ),
  )
  date_joined = models.DateTimeField(_('date joined'), default = timezone.now)
  objects = UserManager()

  EMAIL_FIELD = 'email'
  USERNAME_FIELD = 'email'
  REQUIRED_FIELD = ['first_name', 'last_name']

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')

  def get_full_name(self):
    """Return the first_name plus the last_name, with a space in between."""
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

  def get_short_name(self):
    """Return the short name for the user."""
    return self.first_name

  def email_user(self, subject, message, from_email = None, **kwargs):
    """Send an email to this user."""
    send_mail(subject, message, from_email, [self.email], **kwargs)



# 学生テーブル
class Student(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    primary_key = True,
    related_name="student"
  )
  organization_id = models.ForeignKey(Organization)
  group_id = models.ForeignKey(Group)
  sex_id = models.ForeignKey(Sex)

  school_year = models.IntegerField(_('school year'), blank = True, null = True)
  school_class = models.IntegerField(_('school class'), blank = True, null = True)
  school_number = models.IntegerField(_('school number'), blank = True, null = True)

  def __str__(self):
    return self.user.get_full_name()


# 先生テーブル
class Teacher(models.Model):
  user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    on_delete = models.CASCADE,
    primary_key = True,
    related_name="teacher"
  )
  organization_id = models.ForeignKey(Organization)
  sex_id = models.ForeignKey(Sex)

  def __str__(self):
    return self.user.get_full_name()


