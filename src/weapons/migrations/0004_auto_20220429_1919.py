# Generated by Django 3.2.8 on 2022-04-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0003_auto_20220428_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='product',
            name='num_product',
            field=models.IntegerField(),
        ),
    ]
