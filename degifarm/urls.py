"""degifarm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from submission_form import views as sub_views
from user_page import views as user_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(next_page = 'index'), name = 'logout'),

    url(r'^accounts/$', sub_views.start_service, name = 'service_start'),
    url(r'^accounts/create/$', sub_views.LinkUserCreateView.as_view(), name = 'user_create_link'),
    url(r'^accounts/(?P<uuid>.*)/(?P<uuid_hash>.*)/$', sub_views.UserCreateView.as_view(), name = 'user_create'),

    url(r'^user/', include('user_page.urls')),

    url(r'^$', sub_views.IndexView.as_view(), name = 'index'),
    url(r'^submission_form/', include('submission_form.urls')),
]
