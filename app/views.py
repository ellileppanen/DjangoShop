from django.shortcuts import render, redirect
from .models import Supplier, Product, Store, Stock

def landingview(request):
    return render(request, 'landingpage.html')

# Product views
def productlistview(request):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist, 'suppliers': supplierlist}
    return render (request,"productlist.html",context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def edit_product_get(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_product.html",context)


def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)

# Supplier views
def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render (request,"supplierlist.html",context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def edit_supplier_get(request, id):
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supplier.html",context)


def edit_supplier_post(request, id):
        item = Supplier.objects.get(id = id)
        item.contactname = request.POST['contactname']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.address = request.POST['address']
        item.country = request.POST['country']
        item.save()
        return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)

#Store views
def storelistview(request):
    storelist = Store.objects.all()
    context = {'stores': storelist}
    return render (request,"storelist.html",context)

def addstore(request):
    a = request.POST['storename']
    b = request.POST['storemanager']
    c = request.POST['location']
    d = request.POST['city']
    
    Store(storename = a, storemanager = b, location = c, city = d).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletestore(request, id):
    store = Store.objects.get(id = id)
    context = {'store': store}
    return render (request,"confirmdelsto.html",context)

def deletestore(request, id):
    Store.objects.get(id = id).delete()
    return redirect(storelistview)

def edit_store_get(request, id):
        store = Store.objects.get(id = id)
        context = {'store': store}
        return render (request,"edit_store.html",context)

def edit_store_post(request, id):
        item = Store.objects.get(id = id)
        item.storemanager = request.POST['storemanager']
        item.location = request.POST['location']
        item.city = request.POST['city']
        item.save()
        return redirect(storelistview)

def searchstores(request):
    search = request.POST['search']
    filtered = Store.objects.filter(storename__icontains=search)
    context = {'stores': filtered}
    return render (request,"storelist.html",context)

#Stock views
def stocklistview(request):
    stocklist = Stock.objects.all()
    storelist = Store.objects.all()
    productlist = Product.objects.all()
    context = {'stock': stocklist, 'stores': storelist, 'products': productlist}
    return render (request,"stocklist.html",context)