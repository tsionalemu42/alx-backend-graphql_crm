from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default="example@example.com")
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name
