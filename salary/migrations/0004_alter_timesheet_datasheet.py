# Generated by Django 4.0.4 on 2022-05-02 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_alter_timesheet_datasheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timesheet',
            name='dataSheet',
            field=models.DateField(default='2022-05-02', verbose_name='Дата'),
        ),
    ]
