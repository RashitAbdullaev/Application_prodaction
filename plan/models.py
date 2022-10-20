from django.db import models
from django.contrib.auth.models import User


class Product_type(models.Model):
    product_type = models.CharField(max_length=50, null=True, verbose_name='Тип плана')

    def __str__(self):
        return self.product_type

    class Meta:
        verbose_name_plural = 'Типы продукции'
        verbose_name = 'Тип продукции'


# class Plot(models.Model):
#     plot_name = models.CharField(max_length=150, verbose_name='Название участка')
#     user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Бригадир')
#
#     def __str__(self):
#         return self.plot_name
#
#     class Meta:
#         verbose_name_plural = 'Участок'
#         verbose_name = 'Участок'


class Model_product(models.Model):
    model_name = models.CharField(max_length=50, verbose_name='Модель')
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE, verbose_name='Модель')

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name_plural = 'Модель'
        verbose_name = 'Модель'


class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название продукта')
    product_number = models.CharField(max_length=50, verbose_name='Номер продукта')
    product_type = models.ForeignKey(Product_type, null=False, on_delete=models.PROTECT, verbose_name='Тип продукта')
    model = models.ForeignKey(Model_product, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Модели')

    def __str__(self):
        return '%s %s' % (self.product_name, self.product_number)

    class Meta:
        verbose_name_plural = 'Продукции'
        verbose_name = 'Продукция'


class Worforce(models.Model):
    workforce_surname = models.CharField(max_length=250, verbose_name='Фамилия')
    workforce_name = models.CharField(max_length=250, verbose_name='Имя')
    workforce_patronymic = models.CharField(max_length=250, verbose_name='Отчество')

    def __str__(self):
        return self.workforce_surname

    class Meta:
        verbose_name_plural = 'Коммерсанты'
        verbose_name = 'Каммерсант'


class Buyer(models.Model):
    buyer_name = models.CharField(max_length=250, verbose_name='Наименование заказчика')
    buyer_city = models.CharField(max_length=250, verbose_name='Город заказа')
    buyer_phone = models.IntegerField(verbose_name='Номер телефона')
    buyer_FIO = models.CharField(max_length=300, verbose_name='ФИО')

    def __str__(self):
        return self.buyer_name

    class Meta:
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчик'


class Reserve(models.Model):
    reserve_date = models.DateField(verbose_name='Дата бронирования')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Породкция')
    buyer = models.ForeignKey(Buyer, on_delete=models.PROTECT, verbose_name='Заказчик')
    workforce = models.ForeignKey(Worforce, on_delete=models.PROTECT, verbose_name='Коммерсант')

    class Meta:
        verbose_name_plural = 'Резерв'
        verbose_name = 'Резерв'


class Act(models.Model):
    act_date = models.DateField(verbose_name='Дата сдачи')
    act_note = models.CharField(max_length=250, verbose_name='Примечание')
    forman = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Бригадир')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.product, self.pk)

    class Meta:
        verbose_name_plural = 'Акты'
        verbose_name = 'Акт'


class Plan(models.Model):
    plan_note = models.CharField(max_length=250, verbose_name='Примечание')
    date_merchant = models.DateField(verbose_name='Срок_коммерсанта')
    guild = models.ForeignKey('salary.Department', models.PROTECT, verbose_name='Участок')
    foreman = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Бригадир')
    date_guild = models.DateField(verbose_name='Срок-бригодира', blank=True, null=True)
    product = models.OneToOneField(Product, null=True, on_delete=models.CASCADE, verbose_name='Продукт')
    act = models.ForeignKey(Act, null=True, on_delete=models.CASCADE, verbose_name='Акт', blank=True)
    reserve = models.ForeignKey(Reserve, on_delete=models.PROTECT, verbose_name='Резерв', blank=True, null=True)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'План'
        verbose_name = 'План'


class Product_expense_product(models.Model):
    date_expense = models.DateField(verbose_name='Срок списания', auto_now=True)
    product_one = models.ForeignKey(Product, related_name='Продукция', verbose_name='Продукция',
                                    on_delete=models.CASCADE, blank=True, null=True)
    id_expense_product = models.ForeignKey(Product, verbose_name='Связанная продукция', on_delete=models.CASCADE,
                                           blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Привязка продукции'
        verbose_name = 'Привязка продукции'
