# Generated by Django 3.2.8 on 2022-04-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0005_alter_product_num_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='num_product',
            field=models.CharField(max_length=100, verbose_name='чето там'),
        ),
    ]