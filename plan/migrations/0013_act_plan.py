# Generated by Django 4.0.2 on 2022-08-04 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0012_remove_act_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='plan.plan', verbose_name='План'),
        ),
    ]