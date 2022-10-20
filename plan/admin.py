from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_number', 'product_type', 'model')
    list_display_links = ('product_name', 'product_number', 'product_type', 'model')


class Product_typeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_type')
    list_display_links = ('pk', 'product_type')


class PlanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'plan_note', 'date_merchant', 'date_guild', 'foreman', 'guild', 'product', 'act')
    list_display_links = ('pk', 'plan_note', 'date_merchant', 'date_guild', 'foreman', 'guild', 'product', 'act')


class Model_productAdmin(admin.ModelAdmin):
    list_display = ('pk', 'model_name', 'product_type')
    list_display_links = ('model_name', 'product_type')


class ActAdmin(admin.ModelAdmin):
    list_display = ('pk', 'act_date', 'act_note', 'forman', 'product')
    list_display_links = ('act_date', 'act_note', 'forman', 'product')


class WorkforceAdmin(admin.ModelAdmin):
    list_display = ('workforce_surname', 'workforce_name', 'workforce_patronymic')
    list_display_links = ('workforce_surname', 'workforce_name', 'workforce_patronymic')


class BuyerAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'buyer_city', 'buyer_phone', 'buyer_FIO')
    list_display_links = ('buyer_name', 'buyer_city', 'buyer_phone', 'buyer_FIO')


class ReserveAdmin(admin.ModelAdmin):
    list_display = ('reserve_date', 'product', 'buyer', 'workforce')
    list_display_links = ('reserve_date', 'product', 'buyer', 'workforce')


class Poduct_exponse_productAdmin(admin.ModelAdmin):
    list_display = ('date_expense', 'product_one', 'id_expense_product')
    list_display_links = ('date_expense', 'product_one', 'id_expense_product')


# class PlotAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'plot_name', 'user')
#     list_display_links = ('pk', 'plot_name', 'user')


admin.site.register(Reserve, ReserveAdmin)
# admin.site.register(Plot, PlotAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Worforce, WorkforceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_type, Product_typeAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Model_product, Model_productAdmin)
admin.site.register(Act, ActAdmin)
admin.site.register(Product_expense_product, Poduct_exponse_productAdmin)
