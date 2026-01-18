from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    membership_bzone = 'B'
    membership_silver = 'S'
    membership_gold = 'G'
    MEMBERSHIP_CHOICES = [
        (membership_bzone, 'Bronze'),
        (membership_silver, 'Silver'),
        (membership_gold, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    membership=models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=membership_bzone,
    )

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETED = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETED, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING,
    )

class Address(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)