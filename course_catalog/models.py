from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext as _

class Catalog(models.Model):
    pass

class Course(models.Model):
    pass

class Subject(models.Model):
    pass

class Term(models.Model):  # quarter or semester
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('term_detail', kwargs={'pk': self.pk})


class Semester(Term):
    def get_absolute_url(self):
        return reverse('semester_detail', kwargs={'pk': self.pk})


class Quarter(Term):
    def get_absolute_url(self):
        return reverse('semester_detail', kwargs={'pk': self.pk})


