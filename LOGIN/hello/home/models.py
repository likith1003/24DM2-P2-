from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(("Name"), max_length=50)
    pno=models.CharField(("Phone Number"), max_length=50)
    email=models.EmailField(("Email"), max_length=254)
    gender=models.CharField(("Gender"), max_length=50)
    address=models.CharField(("Address"), max_length=50)
    username=models.CharField(("Username"), max_length=50)
    password=models.CharField(("Password"), max_length=50)
    def __str__(self):
        return self.name
    