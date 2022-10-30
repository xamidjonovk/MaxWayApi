from rest_framework import serializers
from .models import Customer, Order, OrderProduct, Product


class CustomerSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, min_length=12, allow_blank=False, allow_null=False)
    first_name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)
    last_name = serializers.CharField(max_length=100, allow_blank=False, allow_null=False)


class OrderSerializer(serializers.Serializer):
    payment_type = serializers.IntegerField(allow_null=False)
    status = serializers.IntegerField(default=1)
    address = serializers.CharField(allow_null=False, allow_blank=False, max_length=250)


class CustomerOrderSerializer(serializers.Serializer):
    customer = CustomerSerializer(required=True)
    order = OrderSerializer(required=True)
    products = serializers.JSONField()

    def create(self, validated_data):
        customer = validated_data.get("customer")
        phone_number = customer.get("phone_number")

        try:
            customer = Customer.objects.get(phone_number=phone_number)
        except:
            customer = Customer.objects.create(**customer)

        order = validated_data.get("order")
        order['customer_id'] = customer.id
        order = Order.objects.create(**order)
        products = validated_data.get("products")
        products_exist = False

        for product in products:
            try:
                product_model = Product.objects.get(pk=product['id'])
                OrderProduct.objects.create(
                    product=product_model, count=product['count'],
                    order=order, price=product_model.price
                )
                products_exist = True
            except Exception as e:
                print("Error model not exist:", e)

        if not products_exist:
            order.delete()
            return False
        return True
