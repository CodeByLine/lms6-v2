from django.db import models
# from accounts.models import CustomUserManager, CustomUser
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
# from django.dispatch import receiver
from django.utils import timezone
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse

class Academics:
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, name, created_at, updated_at):
        self._name = name
        self._created_at = created_at
        self.updated_at = updated_at

class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('session_detail', kwargs={'pk': self.pk})

class Course(Academics):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    objects = models.Manager()

# class Course(models.Model):
#     id = models.AutoField(primary_key=True)
#     course_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()

    def __str__(self):
        return f'{self.course_name}'

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})


# class Subject(models.Model):
#     id = models.AutoField(primary_key=True)
#     subject_name = models.CharField(max_length=255)
#     course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1, related_name='course_subject')
#     staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='staff_subject')
#     student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='staff_subject')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     objects = models.Manager()
#
#     def __str__(self):
#         return f'{self.subject_name}'
#
#     def get_absolute_url(self):
#         return reverse('course_detail', kwargs={'pk': self.pk})