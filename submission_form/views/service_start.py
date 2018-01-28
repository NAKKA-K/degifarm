from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction

from submission_form.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from submission_form.forms import OrganizationForm, CustomUserCreationForm, TeacherForm

@transaction.atomic
def start_service(request):
  if request.method == 'POST':
    org_form = OrganizationForm(request.POST)
    user_form = CustomUserCreationForm(request.POST)
    teacher_form = TeacherForm(request.POST)

    if org_form.is_valid() and user_form.is_valid() and teacher_form.is_valid():
      org = org_form.save()
      user = user_form.save()

      teacher = teacher_form.save(commit = False)
      teacher.user = user
      teacher.organization_id = org
      teacher.save()

      messages.success(request, '団体が作成されました。ようこそ、でじふぁーむ。へ')
      return redirect('index')
    else:
      messages.error(request, 'データに不備があります')
  else:
    org_form = OrganizationForm()
    user_form = CustomUserCreationForm()
    teacher_form = TeacherForm()

  return render(request, 'service_starter.html', {
    'org_form': org_form,
    'user_form': user_form,
    'teacher_form': teacher_form,
  })

