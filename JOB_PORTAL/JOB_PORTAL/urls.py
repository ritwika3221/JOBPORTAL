"""JOB_PORTAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from JOB.views import *
from django.conf import settings
#for recieving image
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('JOB.urls') ),
    # path('', index,name="index"),
    # path('reqruiter_login/', reqruiter_login,name="reqruiter_login"),
    # path('user_login/', user_login,name="user_login"),
    # path('user_signup/', user_signup,name="user_signup"),
    # path('reqruiter_signup/', reqruiter_signup,name="reqruiter_signup"),
    # path('dashboard/', dashboard,name="dashboard"),
    # path('Rdashboard/', Rdashboard,name="Rdashboard"),
    # path('add_job/', add_job,name="add_job"),
    # path('job_list/', job_list,name="job_list"),
    # path('edit_job/<int:pid>/', edit_job,name="edit_job"),
    # path('edit_studentprofile/<int:pid>/', edit_studentprofile,name="edit_studentprofile"),
    # path('edit_reqruiterprofile/<int:pid>/', edit_reqruiterprofile,name="edit_reqruiterprofile"),
    # path('delete_job/<int:pid>/', delete_job,name="delete_job"),
    # path('delete_candidate/<int:pid>/', delete_candidate,name="delete_candidate"),
    # path('delete_myjob/<int:pid>/', delete_myjob,name="delete_myjob"),
    # path('user_logout/', user_logout,name="user_logout"),
    # path('reqruiter_logout/', reqruiter_logout,name="reqruiter_logout"),
    # path('change_password/', change_password,name="change_password"),
    # path('change_password2/', change_password2,name="change_password2"),
    # path('latest_job/', latest_job,name="latest_job"),
    # # path('latest_job/', latest_job,name="latest_job"),
    # path('apply/<pid>/', apply,name="apply"),
    # path('view_job/', view_job,name="view_job"),    
    # path('candidate_apply/', candidate_apply,name="candidate_apply"),
    # path('contact/', contact,name="contact"),
    # path('searchk/', searchk,name="searchk"),    
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
