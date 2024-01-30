from django.db import models

# Create your models here.
class Branch(models.Model):
    branchId = models.AutoField(primary_key=True,unique=True)
    bname = models.CharField(max_length=255)



class Restaurant(models.Model):
    restaurantId =models.AutoField(primary_key=True,unique=True)
    rname = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)



class Category(models.Model):
    categoryId = models.AutoField(primary_key=True,unique=True)
    cname = models.CharField(max_length=255)
  
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class FoodItem(models.Model):
    foodId = models.AutoField(primary_key=True,unique=True)
    fname = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
class FoodItemStatus(models.Model):
    statusId = models.AutoField(primary_key=True,unique=True)
  
    
    status_name = models.CharField(max_length=255)
    fooditem=models.ForeignKey(FoodItem,on_delete=models.CASCADE)


    
class Customer(models.Model):
    cId=models.AutoField(primary_key=True,unique=True)
  
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phnumber = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    orderId =models.AutoField(primary_key=True,unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    totalprice=models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=255, blank=True, null=True)
    kitchen_status = models.CharField(max_length=255, blank=True, null=True)

    # payment = models.CharField(max_length=300)
    
class User(models.Model):
    userId =models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Register(models.Model):

    email=models.EmailField()
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)
    
    role=models.CharField(max_length=50)