from django.db import models

# Create your models here.
class Entry(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=50)
    phone_no = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='entry')

    def __str__(self) -> str:
        return self.first_name

