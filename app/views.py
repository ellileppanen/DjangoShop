from django.shortcuts import render, redirect
from .models import Supplier, Product, Store, Stock
from django.contrib.auth import authenticate, login, logout



# Product views
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request,"productlist.html",context)

def addproduct(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
        
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Product.objects.get(id = id).delete()
        return redirect(productlistview)

def edit_product_get(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            product = Product.objects.get(id = id)
            context = {'product': product}
            return render (request,"edit_product.html",context)


def edit_product_post(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            item = Product.objects.get(id = id)
            item.unitprice = request.POST['unitprice']
            item.unitsinstock = request.POST['unitsinstock']
            item.save()
            return redirect(productlistview)

def products_filtered(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        filteredproducts = productlist.filter(supplier = id)
        context = {'products': filteredproducts}
        return render (request,"productlist.html",context)

def searchproducts(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Product.objects.filter(productname__icontains=search)
        context = {'products': filtered}
        return render (request,"productlist.html",context)

# Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request,"supplierlist.html",context)

def addsupplier(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Supplier.objects.get(id = id).delete()
        return redirect(supplierlistview)

def edit_supplier_get(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            supplier = Supplier.objects.get(id = id)
            context = {'supplier': supplier}
            return render (request,"edit_supplier.html",context)


def edit_supplier_post(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            item = Supplier.objects.get(id = id)
            item.contactname = request.POST['contactname']
            item.phone = request.POST['phone']
            item.email = request.POST['email']
            item.address = request.POST['address']
            item.country = request.POST['country']
            item.save()
            return redirect(supplierlistview)

def searchsuppliers(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Supplier.objects.filter(companyname__icontains=search)
        context = {'suppliers': filtered}
        return render (request,"supplierlist.html",context)

#Store views
def storelistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        storelist = Store.objects.all()
        context = {'stores': storelist}
        return render (request,"storelist.html",context)

def addstore(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['storename']
        b = request.POST['storemanager']
        c = request.POST['location']
        d = request.POST['city']
        
        Store(storename = a, storemanager = b, location = c, city = d).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletestore(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        store = Store.objects.get(id = id)
        context = {'store': store}
        return render (request,"confirmdelsto.html",context)

def deletestore(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Store.objects.get(id = id).delete()
        return redirect(storelistview)

def edit_store_get(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            store = Store.objects.get(id = id)
            context = {'store': store}
            return render (request,"edit_store.html",context)

def edit_store_post(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            item = Store.objects.get(id = id)
            item.storemanager = request.POST['storemanager']
            item.location = request.POST['location']
            item.city = request.POST['city']
            item.save()
            return redirect(storelistview)

def searchstores(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        search = request.POST['search']
        filtered = Store.objects.filter(storename__icontains=search)
        context = {'stores': filtered}
        return render (request,"storelist.html",context)

#Stock views
def stocklistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        stocklist = Stock.objects.all()
        storelist = Store.objects.all()
        productlist = Product.objects.all()
        context = {'stock': stocklist, 'stores': storelist, 'products': productlist}
        return render (request,"stocklist.html",context)

def addstock(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        a = request.POST['store']
        b = request.POST['product']
        c = request.POST['quantity']
        Stock(
            store=Store.objects.get(id=a),
            product=Product.objects.get(id=b),
            quantity=c
        ).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletestock(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        stock = Stock.objects.get(id=id)
        context = {
            'stock': stock,
            'product': stock.product,
            'store': stock.store
        }
        return render(request, "confirmdelstock.html", context)

def deletestock(request, id):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        Stock.objects.get(id = id).delete()
        return redirect(stocklistview)

def edit_stock_get(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            stock = Stock.objects.get(id = id)
            context = {'stock': stock}
            return render (request,"edit_stock.html",context)

def edit_stock_post(request, id):
        if not request.user.is_authenticated:
            return render(request, 'loginpage.html')
        else:
            item = Stock.objects.get(id = id)
            item.quantity = request.POST['quantity']
            item.save()
            return redirect(stocklistview)

#logged in 
def landingview(request):
    return render(request, 'landingpage.html')

#login 
def loginview(request):
     return render(request, 'loginpage.html')

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')