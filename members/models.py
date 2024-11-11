from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Products(models.Model):
    Clave = models.CharField(max_length=255)
    Descripcion = models.CharField(max_length=255)
    Linea = models.CharField(max_length=255)
    existencias = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.Descripcion} Linea: {self.Linea}"
