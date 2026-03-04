from django.urls import path
from .views import home_view, product_list_view, product_detail_view

urlpatterns = [
    path("", home_view, name="home"),
    path('products/', product_list_view, name='product_list'),
    path('products/<slug:slug>/', product_detail_view, name='product_detail'),
]
