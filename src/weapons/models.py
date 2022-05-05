import uuid

from django.db import models
# import datetime

categorys = [
    ('Ножи', 'Ножи'),
    ('Оружие', 'Оружие'),
    ('Наклейки', 'Наклейки'),
    ('Аксессуары', 'Аксессуары'),
    ('Одежда', 'Одежда'),
]





class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=False, verbose_name='Название продукта', null=True)
    text = models.TextField(max_length=135, unique=False, verbose_name='Описание продукта', null=True)
    img = models.ImageField(unique=False, verbose_name='Изображение продукта', upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=50, unique=False,  verbose_name='Категория продукта', choices=categorys, blank=False, default='Одежда', null=True)
    link_product = models.CharField(max_length=100, unique=False, verbose_name='Ссылка на продукт', null=True)
    date = models.DateTimeField(verbose_name='дата', null=True)
    num_product = models.IntegerField(verbose_name='чето там')
    # def num(self, name_product):
    #     qs = Product.objects.all()
    #     num = 0
    #     dict = {}
    #     for i in qs:
    #         num += 1
    #         if i.name == name_product:
    #             dict[i.name] = num
    #             return dict[i.name_product]

        #     num += 1
        #     dict[i.name] = num
        # return dict[i.name_product]

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name





