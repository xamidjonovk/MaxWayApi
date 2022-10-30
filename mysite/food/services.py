from contextlib import closing
from collections import OrderedDict
from django.db import connection
from rest_framework.exceptions import NotFound

import json
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))

def get_category_products():
    category_products = query_category_products()
    items = []
    for category_product in category_products:
        items.append(
            OrderedDict(
                {
                    "id": category_product['id'],
                    "title": category_product['title'],
                    "products": json.loads(category_product['products']),
                    "slug": category_product['slug']
                }
            )
        )
    return items

def query_category_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""
        with table1 as (SELECT c.*, (SELECT JSONB_AGG(v) FROM (SELECT food_product.* FROM food_product WHERE 
        food_product.category_id = c.id) v) AS products FROM food_category c)
        select table1.* from table1 where table1.products is not null;
        """)
        category_products = dictfetchall(cursor)
    return category_products

def query_customer(phone_number):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" 
            SELECT * from food_customer WHERE food_customer.phone_number = %s
        """, [phone_number])
        customer = dictfetchone(cursor)
    return customer

def get_customer_by_phone(phone_number):
    customer = query_customer(phone_number)
    return OrderedDict(
        {
            "id": customer['id'],
            "first_name": customer['first_name'],
            "last_name": customer['last_name'],
            "phone_number": customer['phone_number']
        }
    )

def get_products_by_ids(ids):
    with closing(connection.cursor()) as cursor:
        cursor.execute(
            f"""SELECT * FROM food_product WHERE id in ({str(ids).strip("[]")})"""
        )
        products = dictfetchall(cursor)
    return products

