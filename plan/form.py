import json
from django.forms import ModelForm
from django import forms
from .models import *
from django import forms
from salary.models import Department


class Type_productForm(ModelForm):
    class Meta:
        model = Product_type
        fields = ('product_type',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].lable = None


class ProductForm(ModelForm):
    plan_note = forms.CharField(label='Примечание')
    date_merchant = forms.CharField(label='Дата заявки',
                                    widget=forms.TextInput(attrs={'class': 'date', 'type': 'date'}))
    date_guild = forms.CharField(label='Дата Бригадира',
                                 widget=forms.TextInput(attrs={'class': 'date', 'type': 'date'}))
    foreman = forms.ModelChoiceField(queryset=User.objects.all(), label='Бригадир')
    guild = forms.ModelChoiceField(queryset=Department.objects.all(), label='Участок')
    product_number = forms.CharField(label="Номер продукта")
    product_type = forms.ModelChoiceField(label='Тип материала',
                                          widget=forms.widgets.Select(attrs={'class': 'type_product'}),
                                          queryset=Product_type.objects.all()
                                          )

    class Meta:
        model = Product
        fields = ('product_type', 'product_name', 'product_number', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].lable = None


class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ('plan_note', 'date_merchant', 'date_guild', 'foreman','guild',)


class ModelForm(ModelForm):
    class Meta:
        model = Model_product
        fields = ('model_name',)


class ActForm(ModelForm):
    act_date = forms.CharField(label='Дата сдачи',
                               widget=forms.TextInput(attrs={'class': 'date', 'type': 'date'}))

    class Meta:
        model = Act
        fields = ('act_date', 'act_note', 'forman')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].lable = None


class Product_expense_productForm(ModelForm):
    class Meta:
        model = Product_expense_product
        fields =()