"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import landingview, productlistview, supplierlistview, addsupplier, addproduct, \
    deleteproduct, confirmdeleteproduct, deletesupplier, confirmdeletesupplier, edit_product_get, \
    edit_product_post, edit_supplier_get, edit_supplier_post, searchsuppliers, products_filtered, \
    storelistview, stocklistview, addstore, deletestore, confirmdeletestore, edit_store_get, edit_store_post, \
    searchstores

urlpatterns = [
    path('', landingview),

    #product url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),


    #suppliers url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    path('search-suppliers/', searchsuppliers),

    #store url's
    path('stores/', storelistview),
    path('add-store/', addstore),
    path('delete-store/<int:id>/', deletestore),
    path('confirm-delete-store/<int:id>/', confirmdeletestore),
    path('edit-store-get/<int:id>/', edit_store_get),
    path('edit-store-post/<int:id>/', edit_store_post),
    path('search-stores/', searchstores),

    #stock url's
    path('stock/', stocklistview),
]
