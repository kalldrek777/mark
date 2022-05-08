# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
from weapons.models import Product
import psycopg2

class Market777Pipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host='ec2-54-220-243-77.eu-west-1.compute.amazonaws.com',
            user='jtfxiruheopehc',
            password='f93d86c9bcc85e3677007586f785d19d5fcd9e95b5e496462586cbac1513e3f2',
            database='de5kv7me27d4h2',
        )
        self.curr = self.conn.cursor()
        # self.curr.execute("""DELETE FROM weapons_product WHERE id IN (obj.id)""")

    def create_table(self):
        # self.curr.execute('''DROP TABLE IF EXISTS img_tb''')
        # self.curr.execute('''CREATE TABLE img_tb(id INTEGER PRIMARY KEY NOT NULL, src VARCHAR(100))''')
        self.curr.execute('''DROP TABLE IF EXISTS example''')
        self.curr.execute('''CREATE TABLE example(
            id serial PRIMARY KEY,
            src VARCHAR(100))''')
        # self.curr.execute('''CREATE TABLE example(id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, src VARCHAR(100))''') mysql


        # ДОБАВЛЕНИЕ СТОЛБЦА
        # self.curr.execute("""ALTER TABLE weapons_product DROP COLUMN img_produts2 """)
        # self.curr.execute("""ALTER TABLE weapons_product ADD COLUMN img_produts2 TEXT""")
        # УДАЛЕНИЕ СТОЛБЦОВ
        # self.curr.execute("""DELETE FROM weapons_product WHERE id IN (23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42)""")
        # УДАЛЕНИЕ КОЛОНОК
        # self.curr.execute("""CREATE TABLE weapons_product_temp3(id INTEGER PRIMARY KEY NOT NULL, name VARCHAR(100),
        # img VARCHAR(100), category VARCHAR(50), link_product VARCHAR(100), DATE DATETIME, TEXT TEXT, img_produts2
        # TEXT)""")
        # self.curr.execute("""INSERT INTO weapons_product_temp3(id, name, img, category, link_product, DATE, TEXT,
        # img_produts2) SELECT id, name, img, category, link_product, DATE, TEXT, img_produts2 FROM
        # weapons_product""")
        # self.curr.execute("""DROP TABLE weapons_product""")
        # self.curr.execute("""ALTER TABLE weapons_product_temp3 RENAME TO weapons_product""")

    def process_item(self, item, spider):
        self.store_db(item)
        print('Pipeline:' + item['img_url'])
        for i in item:
            print(item[i])
        return item

    def store_db(self, item):
        qs = Product.objects.all()

        self.curr.execute('''insert into example(src) VALUES(%s)''', (
            item['img_url'],
        ))
        self.curr.execute('''UPDATE weapons_product SET
                             img = (SELECT example.src FROM example where weapons_product.num_product = example.id)  
                ''')

        # self.curr.execute('''insert into example(src) VALUES)''', (
        #     item['img_url'],
        # ))
        # self.curr.execute('''UPDATE weapons_product SET
        #                  img = (SELECT example.src FROM example where weapons_product.num_product = example.id)  # w_p id = порядковый номер
        #     ''')


        # inner join - связывание таблиц по общему признаку


        self.conn.commit()