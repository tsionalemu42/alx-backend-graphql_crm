from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    last_order_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
