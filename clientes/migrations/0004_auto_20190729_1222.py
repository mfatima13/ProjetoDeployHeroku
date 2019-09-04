# Generated by Django 2.2.2 on 2019-07-29 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Person')),
                ('produtos', models.ManyToManyField(blank=True, to='clientes.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='doc',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Documento'),
        ),
    ]
