import time

from django.contrib import admin
from weapons.models import Product
import os
from sqlalchemy import create_engine
import subprocess


class ProductAdmin(admin.ModelAdmin):
    exclude = ['img']

    # def save_model(self, request, obj, form, change):
    #
    #         create_engine('sqlite:///C:\Django_Projects\Market\src\db.sqlite3', connect_args={'timeout': 150})
    #         os.system('Scrapy crawl market77')


    # def crawl(self, *args, **kwargs):
    #     super(ProductAdmin, self).save(*args, **kwargs)


        # super(ProductAdmin, self).save_model(request, obj, form, change)
        # os.system('Scrapy crawl market77')

admin.site.register(Product, ProductAdmin)















