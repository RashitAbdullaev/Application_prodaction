# Generated by Django 4.1 on 2022-10-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0019_alter_timesheet_datasheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='dataSheet',
            field=models.DateField(default='2022-10-10', verbose_name='Дата'),
        ),
    ]