from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Documento(models.Model):
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.cpf

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
<<<<<<< HEAD

    class Meta:
        permissions = (
            ('atualizar_clientes', 'Atualizar clientes'),
            ('excluir_clientes', 'excluir clientes'),
        )
=======
>>>>>>> 8c07669162aa3f3460f16081fa2c03c066068a25

    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    numero = models.CharField(max_length=7)
    valor = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=7, decimal_places=2)
    impostos = models.DecimalField(max_digits=7, decimal_places=2)
    pessoa = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    produtos = models.ManyToManyField(Produto, null=False, blank=True)
    nfe_emitida = models.BooleanField(default=False)

    def get_total(self):
        tot = 0
        for produto in self.produtos.all():
            tot += produto.preco
        return (tot - self.desconto) - self.impostos
    
    def __str__(self):
        return self.numero

@receiver(m2m_changed, sender=Venda.produtos.through)# through = ao decorrer dos elementos pertencentes a esse relacionamento
def update_vendas_total(sender, instance, **kwargs):
    instance.valor = instance.get_total()
    instance.save()
