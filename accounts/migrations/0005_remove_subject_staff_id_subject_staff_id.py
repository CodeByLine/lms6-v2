# Generated by Django 4.0.4 on 2022-04-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='staff_id',
        ),
        migrations.AddField(
            model_name='subject',
            name='staff_id',
            field=models.ManyToManyField(related_name='staff', to='accounts.staff'),
        ),
    ]