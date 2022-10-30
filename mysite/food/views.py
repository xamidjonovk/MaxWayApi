from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . import services
from rest_framework.exceptions import NotFound
from .serializers import CustomerOrderSerializer

class CategoryProductsView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        category_products = services.get_category_products()
        return Response(category_products)

class CustomerView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        print(request.data)
        if not phone_number:
            raise NotFound("Mavjud emas")
        customer = services.get_customer_by_phone(phone_number)
        return Response(customer)

class CustomerOrder(GenericAPIView):
    def post(self, request):
        serializer = CustomerOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ProductView(GenericAPIView):
    def get(self, request):
        ids = request.query_params.getList("ids[]")
        if not ids:
            raise NotFound("Empty array")
        products = services.get_products_by_ids(ids)
        return Response(products)
