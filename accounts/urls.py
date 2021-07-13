from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customers,name="customer"),

    path('create_order/<str:pk>/', views.create_orders,name="create_order"),
    path('update_order/<str:pk>/', views.update_orders,name="update_order"),
    path('delete_order/<str:pk>', views.delete_orders,name="delete_order"),
]