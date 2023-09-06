# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressid = models.IntegerField(primary_key=True)
    addressline1 = models.CharField(max_length=60, blank=True, null=True)
    addressline2 = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    postalcode = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Creditcard(models.Model):
    creditcardid = models.IntegerField(primary_key=True)
    cardtype = models.CharField(max_length=50, blank=True, null=True)
    cardnumber = models.CharField(max_length=25, blank=True, null=True)
    expmonth = models.SmallIntegerField(blank=True, null=True)
    expyear = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditcard'


class Customer(models.Model):
    customerid = models.IntegerField(primary_key=True)
    personid = models.ForeignKey('Person', models.DO_NOTHING, db_column='personid', blank=True, null=True)
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='storeid', blank=True, null=True)
    territoryid = models.ForeignKey('Salesterritory', models.DO_NOTHING, db_column='territoryid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Person(models.Model):
    businessentityid = models.IntegerField(primary_key=True)
    persontype = models.CharField(max_length=2, blank=True, null=True)
    namestyle = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=8, blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    emailpromotion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Personcreditcard(models.Model):
    personcreditcardid = models.AutoField(primary_key=True)
    businessentityid = models.ForeignKey(Person, models.DO_NOTHING, db_column='businessentityid', blank=True, null=True)
    creditcardid = models.ForeignKey(Creditcard, models.DO_NOTHING, db_column='creditcardid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personcreditcard'


class Product(models.Model):
    productid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    productnumber = models.CharField(max_length=25, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    safetystocklevel = models.SmallIntegerField(blank=True, null=True)
    reorderpoint = models.SmallIntegerField(blank=True, null=True)
    standardcost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    listprice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    size = models.CharField(max_length=5, blank=True, null=True)
    sizeunitmeasurecode = models.CharField(max_length=3, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    daystomanufacture = models.IntegerField(blank=True, null=True)
    productsubcategoryid = models.ForeignKey('Productsubcategory', models.DO_NOTHING, db_column='productsubcategoryid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Productcategory(models.Model):
    productcategoryid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productcategory'


class Productsubcategory(models.Model):
    productsubcategoryid = models.IntegerField(primary_key=True)
    productcategoryid = models.ForeignKey(Productcategory, models.DO_NOTHING, db_column='productcategoryid', blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productsubcategory'


class Salesorderdetails(models.Model):
    salesorderdetailid = models.IntegerField(primary_key=True)
    salesorderid = models.ForeignKey('Salesorderheader', models.DO_NOTHING, db_column='salesorderid', blank=True, null=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='productid', blank=True, null=True)
    carriertrackingnumber = models.CharField(max_length=25, blank=True, null=True)
    orderqty = models.SmallIntegerField(blank=True, null=True)
    specialofferid = models.IntegerField(blank=True, null=True)
    unitprice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unitpricediscount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesorderdetails'


class Salesorderheader(models.Model):
    salesorderid = models.IntegerField(primary_key=True)
    revisionnumber = models.SmallIntegerField(blank=True, null=True)
    orderdate = models.DateTimeField(blank=True, null=True)
    duedate = models.DateTimeField(blank=True, null=True)
    shipdate = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    onlineorderflag = models.BooleanField(blank=True, null=True)
    purchaseordernumber = models.CharField(max_length=25, blank=True, null=True)
    accountnumber = models.CharField(max_length=15, blank=True, null=True)
    customerid = models.IntegerField(blank=True, null=True)
    territoryid = models.ForeignKey('Salesterritory', models.DO_NOTHING, db_column='territoryid', blank=True, null=True)
    shiptoaddressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='shiptoaddressid', blank=True, null=True)
    creditcardid = models.ForeignKey(Creditcard, models.DO_NOTHING, db_column='creditcardid', blank=True, null=True)
    subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    taxamt = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    freight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    totaldue = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    comment = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'salesorderheader'


class Salesterritory(models.Model):
    territoryid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    countryregioncode = models.CharField(max_length=3, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)
    salesytd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    saleslastyear = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    costytd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    costlastyear = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesterritory'


class Store(models.Model):
    businessentityid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    salespersonid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store'
