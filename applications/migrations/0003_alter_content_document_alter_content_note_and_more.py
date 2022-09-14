# Generated by Django 4.1 on 2022-09-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_content_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Документ'),
        ),
        migrations.AlterField(
            model_name='content',
            name='note',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='content',
            name='text_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Порядковый номер'),
        ),
    ]
