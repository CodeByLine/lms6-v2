# Generated by Django 4.0.4 on 2022-04-21 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_subject_staff_id_subject_staff_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='staff_id',
            field=models.ManyToManyField(related_name='staffs', to='accounts.staff'),
        ),
    ]