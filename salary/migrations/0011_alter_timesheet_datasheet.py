# Generated by Django 4.0.4 on 2022-06-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0010_rename_date_coefficient_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='dataSheet',
            field=models.DateField(default='2022-06-07', verbose_name='Дата'),
        ),
    ]