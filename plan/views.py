import datetime
import json
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from rest_framework.response import Response
from .models import *
from django.urls import reverse_lazy
from .form import ProductForm, PlanForm, ModelForm, ActForm, Product_expense_productForm
from rest_framework import generics
from .serializers import PlanSerializer, ProductSerializer


class ListPlan(ListView):
    model = Product_type
    template_name = 'plan/product_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        today = datetime.date.today()
        context['plan'] = Plan.objects.filter(date_merchant__month=str(today.month),
                                              date_merchant__year=str(today.year)).order_by(
            'foreman'
        )

        return context


class DatePlan(ListView):
    model = Plan
    template_name = 'plan/plan_date.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_date'] = Plan.objects.filter(date_merchant__year=self.kwargs['date'][0:4],
                                                   date_merchant__month=self.kwargs['date'][5:7]
                                                   )

        return context


class AllPlan(ListView):
    model = Plan
    template_name = 'plan/all_plan.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_all'] = Plan.objects.select_related('product')
        return context


class CustomSuccessMessageMixin:

    @property
    def success_msg(self):
        return False

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return '%s?id=%s' % (self.success_url, self.object.id)


class Add(CustomSuccessMessageMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'plan/plan_create.html'
    success_url = reverse_lazy('plan:list_plan')
    success_msg = 'План добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_all'] = Product_type.objects.all()
        return context

    def form_valid(self, form):
        print(self.request.POST['model'])
        if self.request.POST['model'].isdigit():
            form.instance.model_id = self.request.POST['model']
        else:
            form.instance.model_id = ''
        plan_all = PlanForm(self.request.POST)
        product = Product_expense_productForm(self.request.POST)
        form.save()
        plan_all.instance.product_id = Product.objects.last().pk
        plan_all.save()
        print(type(self.request.POST['product']))
        if self.request.POST['product'].isdigit():
            product.instance.product_one_id = Product.objects.last().pk
            product.instance.id_expense_product_id = self.request.POST['product']
            product.save()
        return super().form_valid(form)


class UpdateProduct(CustomSuccessMessageMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'plan/update_plan.html'
    success_url = reverse_lazy('plan:list_plan')
    success_msg = 'План обновлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.save()
        product = self.get_object().id

        Plan.objects.filter(Q(act=None) & Q(guild=self.request.POST['guild'])).update(
            foreman=self.request.POST['foreman'])

        Plan.objects.filter(product=product).update(plan_note=self.request.POST['plan_note'],
                                                    date_merchant=self.request.POST['date_merchant'],
                                                    )
        return super().form_valid(form)


class Plan_delete(CustomSuccessMessageMixin, DeleteView):
    model = Product
    template_name = 'plan/delete_plan.html'
    success_url = reverse_lazy('plan:list_plan')
    success_msg = 'План удален'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.kwargs['pk']
        return context


class Model_create(CustomSuccessMessageMixin, CreateView):
    model = Model_product
    form_class = ModelForm
    template_name = 'plan/create_model.html'
    success_url = reverse_lazy('plan:list_plan')
    success_msg = 'Модель добавлена'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_model'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.product_type_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)


class Act_view(ListView):
    model = Plan
    template_name = 'plan/akt_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plan_all'] = Plan.objects.all()
        return context


class Act_data_view(ListView):
    model = Act
    template_name = 'plan/act_data_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['act_data'] = Act.objects.filter(product=self.kwargs['pk'])
        return context


class Act_create(CustomSuccessMessageMixin, CreateView):
    model = Act
    template_name = 'plan/act_create.html'
    form_class = ActForm
    success_url = reverse_lazy('plan:list_plan')
    success_msg = 'Акт добавлен'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        form.save()
        Plan.objects.filter(product_id=self.kwargs['pk']).update(act_id=Act.objects.last().pk)
        return super().form_valid(form)


class AddJsonApi(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        data1 = "001"
        my_list = list()
        my_list_pk = list()

        if Product.objects.filter(product_type=data['type_id']):
            for i in Product_type.objects.filter(product_type=data['type_name']):
                product = i.product_type
            for j in Product.objects.filter(product_type=data['type_id']):
                product_number = j.product_number
                number = int(product_number.split('.')[1]) + 1
                sort_date = product.split('.')[0] + "." + str(f'{number:03}')
            for k in Model_product.objects.filter(product_type=data['type_id']):
                my_list.append(k.model_name)
                my_list_pk.append(k.pk)
            data = {
                'model_pk': my_list_pk,
                'model': my_list,
                'type_name': sort_date,
                'type_id': data['type_id'],
            }

        else:
            for i in Product_type.objects.filter(product_type=data['type_name']):
                product = i.product_type
                sort_date = product.split('.')[0] + "." + data1
            for k in Model_product.objects.filter(product_type=data['type_id']):
                my_list.append(k.model_name)
                my_list_pk.append(k.pk)
            data = {
                'model_pk': my_list_pk,
                'model': my_list,
                'type_name': sort_date,
                'type_id': data['type_id'],
            }

        return Response(data)


class UpdateJsonApi(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        for i in Plan.objects.filter(product=data['type_id']):
            plan_note = i.plan_note
            date_merchant = i.date_merchant
            date_guild = i.date_guild
            foreman = i.foreman.pk
            guild = i.guild.pk

            data = {
                'type_id': data['type_id'],
                'plan_note': plan_note,
                'date_merchant': date_merchant,
                'date_guild': date_guild,
                'foreman': foreman,
                'guild': guild
            }

        return Response(data)


class Product_exponseJsonApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        my_list = list()
        my_list_pk = list()
        for k in Product.objects.filter(product_type=data['type_id']):
            my_list.append(k.product_name)
            my_list_pk.append(k.pk)
        data = {
            'product_pk': my_list_pk,
            'product': my_list,
            'type_id': data['type_id'],
        }

        return Response(data)
