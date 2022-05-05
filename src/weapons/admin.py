import profile
import time


from django.contrib import admin
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from weapons.models import Product
import subprocess
from django.contrib import admin
from django_object_actions import DjangoObjectActions
import os
import mysql.connector


class ProductAdmin(DjangoObjectActions, admin.ModelAdmin):
    # change_list_template = 'weapons/templates/admin/weapons/product/model_change_list.html'
    exclude = ['img', 'num_product']
    list_display = ["name", "link_product"]

    def save_model(self, request, obj, form, change):
        qs = Product.objects.all()
        num = 1
        dict = {}
        for i in qs:
            num += 1
        print(num)
        obj.num_product = num
        super().save_model(request, obj, form, change)

    def get(modeladmin, request, queryset):
        os.system('Scrapy crawl market77')

    changelist_actions = ('get',)

    def __str__(self):
        return self.name


admin.site.register(Product, ProductAdmin)










