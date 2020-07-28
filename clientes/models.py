from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(null=True, blank=True, max_digits=5, decimal_places=2)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name