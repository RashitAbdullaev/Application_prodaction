# Generated by Django 4.0.2 on 2022-04-29 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=50, null=True, verbose_name='Тип плана')),
            ],
            options={
                'verbose_name': 'Тип продукции',
                'verbose_name_plural': 'Типы продукции',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('product_number', models.IntegerField(verbose_name='Номер продукта')),
                ('guild', models.CharField(choices=[('Основной 57', 'Основной 57'), ('Основной 50', 'Основной 50')], default='Основной 50', max_length=25, verbose_name='Участок')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plan.product_type', verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name': 'Продукция',
                'verbose_name_plural': 'Продукции',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_note', models.CharField(max_length=250, verbose_name='Примечание')),
                ('date', models.DateField(verbose_name='Сроки')),
                ('foreman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'План',
            },
        ),
        migrations.CreateModel(
            name='Model_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, verbose_name='Модель')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.product_type', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модель',
            },
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_number', models.IntegerField(verbose_name='Номер акта')),
                ('act_date', models.DateField(verbose_name='Срок изготовления')),
                ('act_note', models.CharField(max_length=250, verbose_name='Примечание')),
                ('forman', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Бригадир')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plan.plan', verbose_name='План')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Акт',
                'verbose_name_plural': 'Акты',
            },
        ),
    ]