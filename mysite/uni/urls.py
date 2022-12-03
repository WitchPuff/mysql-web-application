from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student', views.StudentQuery, name='StudentQuery'),
    path('course', views.CourseQuery, name='CourseQuery'),
    path('failed', views.failed, name='failed'),
    path('reg_stu', views.RegStu, name='RegStu'),
    path('reg_inst', views.RegInst, name='RegInst'),




]