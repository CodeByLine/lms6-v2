
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext as _

from accounts.models import CustomUser


class SessionYearModel(models.Model):
	id = models.AutoField(primary_key=True)
	session_start_year = models.DateField()
	session_end_year = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def get_absolute_url(self):
		return reverse('session_detail', kwargs={'pk': self.pk})


class Course(models.Model):
	id = models.AutoField(primary_key=True)
	course_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def __str__(self):
		return f'{self.course_name}'

	def get_absolute_url(self):
		return reverse('course_detail', kwargs={'pk': self.pk})


class Subject(models.Model):
	id = models.AutoField(primary_key=True)
	subject_name = models.CharField(max_length=255)
	course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1, related_name='course_subject')
	staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='staff_subject')
	student_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1, related_name='student_subject')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	objects = models.Manager()

	def __str__(self):
		return f'{self.subject_name}'
	
	def get_absolute_url(self):
		return reverse('course_detail', kwargs={'pk': self.pk})
