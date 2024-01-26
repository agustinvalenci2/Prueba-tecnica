"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import *
urlpatterns = [
         path('admin/', admin.site.urls),
    path('liststudents/', list_students),
    path('addstudent/',add_student),
    path('getstudent/<int:id>',get_student),
    path('listteachers/', list_teachers),
    path('addteacher/',add_teacher),
    path('getteacher/<int:id>',get_teacher),
    path('listhours/<int:subject_id>/', list_hours),
    path('addhour/',add_hour),
    path('gethour/<int:id>',get_hour),
    path('listsubjects/<int:student_id>', list_subjects),
    path('addsubject/',add_subject),
    path('getsubject/<int:id>',get_subject),
    path('getenrolled/<int:student_id>',get_enrolled),
    path('getbyteacher/<int:teacher_id>',get_by_teacher),
    path('searchstudentsbyname/',search_students_by_name),
    path('enroll/',enroll),
    path('getassistant/<int:student_id>/<int:subject_id>/',get_assistant),
]
