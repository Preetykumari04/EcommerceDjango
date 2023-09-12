from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    phoneno=models.IntegerField()
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    status=models.IntegerField(default=1)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    offerp = models.IntegerField()
    image = models.ImageField(upload_to="product/")

class MenShirt(Product):
    author = models.CharField(max_length=100)

class MenTShirt(Product):
    author = models.CharField(max_length=100)

class MenJeans(Product):
    author = models.CharField(max_length=100)

class WomenKurti(Product):
    author = models.CharField(max_length=100)

class WomenTop(Product):
    author = models.CharField(max_length=100)

class WomenJeans(Product):
    author = models.CharField(max_length=100)

class KidBoys(Product):
    author = models.CharField(max_length=100)

class KidGawn(Product):
    author = models.CharField(max_length=100)

class KidSummer(Product):
    author = models.CharField(max_length=100)

class CartItem(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)  # Add this line
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Add more fields as needed, such as user reference for tracking cart items per user

class Order(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)  # Add this line
    products = models.ManyToManyField(Product, through='OrderedItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderedItem(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)  # Add this line
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
