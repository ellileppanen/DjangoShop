from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length = 50, default="firma")
    contactname = models.CharField(max_length = 50, default="firma")
    address = models.CharField(max_length = 100, default="firma")
    phone = models.CharField(max_length = 20, default="firma")
    email = models.CharField(max_length = 50, default="firma")
    country = models.CharField(max_length = 50, default="firma")

    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
    
class Store(models.Model):
    storename = models.CharField(max_length = 50, default="kauppa")
    storemanager = models.CharField(max_length = 50, default="henkilö")
    location = models.CharField(max_length = 100, default="sijainti")
    city = models.CharField(max_length = 30, default="kaupunki")

    def __str__(self):
        return f"{self.storename} managed by {self.storemanager} in {self.city}"

class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.productname} in {self.store.storename}"