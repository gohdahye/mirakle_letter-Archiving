from django.urls import path
from . import views

app_name = "myshop"

urlpatterns = [
    path('retry_order/<int:order_id>', views.retry_order, name='retry_order'),
    path('', views.home, name="pay_home"),
]
