# Generated by Django 2.2.3 on 2019-08-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190801_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='nfe_emitida',
            field=models.BooleanField(default=False),
        ),
    ]
