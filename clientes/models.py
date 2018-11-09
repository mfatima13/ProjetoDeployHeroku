from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clints_photos', null=True, blank=True) # upload_to cria um diretorio para as imagens dessa classe

    def __str__(self):
        return self.first_name + ' ' + self.last_name

