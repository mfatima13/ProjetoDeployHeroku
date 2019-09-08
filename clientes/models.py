from django.db import models

class Documento(models.Model):
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.cpf

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clints_photos', null=True, blank=True) # upload_to cria um diretorio para as imagens dessa classe
    doc = models.OneToOneField(Documento, null=True, blank=True, on_delete=models.CASCADE)

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name

