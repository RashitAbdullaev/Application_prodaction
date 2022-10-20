from django.urls import path
from .views import ListPlan, Add, AddJsonApi, UpdateProduct, Plan_delete, AllPlan, DatePlan, Model_create, Act_view, \
    UpdateJsonApi, Act_create, Product_exponseJsonApi,Act_data_view

app_name = 'plan'
urlpatterns = [
    path('', ListPlan.as_view(), name="list_plan"),
    path('all_plan', AllPlan.as_view(), name="all_plan"),
    path('plan/<str:date>', DatePlan.as_view(), name="date_plan"),
    path('add', Add.as_view(), name="add"),
    path('add_json', AddJsonApi.as_view(), name="add_json"),
    path('update_json', UpdateJsonApi.as_view(), name="update_json"),
    path('update_plan/<int:pk>', UpdateProduct.as_view(), name="update_product"),
    path('delete_plan/<int:pk>', Plan_delete.as_view(), name="delete_plan"),
    path('create_model/<int:pk>', Model_create.as_view(), name="model_create"),
    path('act', Act_view.as_view(), name="act_view"),
    path('act_create/<int:pk>', Act_create.as_view(), name='act_create'),
    path('product_expense', Product_exponseJsonApi.as_view(), name='product_expense_api'),
    path('act_data_view/<int:pk>', Act_data_view.as_view(), name='act_data_view')
]
