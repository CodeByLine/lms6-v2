# Generated by Django 4.0.4 on 2022-04-20 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_subject_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Student')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='subject',
            name='staff_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='staff_subject', to=settings.AUTH_USER_MODEL),
        ),
    ]
