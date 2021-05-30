"""BM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', admin.site.urls),
    path('home', views.home),
    path('product', views.product_list),
    path('product/<int:pk>', views.product_detail),
    path('company', views.company_list),
    path('company/<int:pk>',views.company_detail),
    path('company/filter',views.company_filter),
    path('company/product/<int:pk>',views.company_product),
    path('category',views.category_list),
    path('category/<int:pk>',views.category_detail),
    path('category/filter',views.category_filter),
    path('category/product/<int:pk>',views.category_product),
    path('prodType',views.prodType_list),
    path('prodType/<int:pk>',views.prodType_detail),
    path('prodType/filter',views.prodType_filter),
    path('prodType/product/<int:pk>',views.prodType_product),
    path('state',views.state_list),
    path('state/<int:pk>',views.state_detail),
    path('state/filter',views.state_filter),
    path('state/product/<int:pk>',views.state_product),
    # path('company/filter/count',views.company_count),
    path('customer', views.customer_list),
    # path('product/state', views.product_state),
]
