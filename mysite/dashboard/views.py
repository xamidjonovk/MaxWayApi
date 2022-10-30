from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound
from food.models import *
from .serializers import *
from rest_framework.response import Response


class CategoryView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = Category.objects.get(pk=pk)
        except Exception:
            raise NotFound("Not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = CategorySerializer(model, many=False)
            return Response(serializer.data)

        else:
            model = Category.objects.all()
            serializer = CategorySerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = CategorySerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, requests, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delate()
        return Response({"state": "deleted"})


class ProductView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = Product.objects.get(pk=pk)
        except Exception:
            return NotFound("Not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = ProductSerializer(model, many=False)
            return Response(serializer.data)

        else:
            model = Product.objects.all()
            serializer = ProductSerializer(model, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = ProductSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, requests, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delate()
        return Response({"state": "deleted"})


class OrderView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = Order.objects.get(pk=pk)
        except Exception:
            return NotFound("Not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = OrderSerializer(model, many=False)
            return Response(serializer.data)

        else:
            model = Order.objects.all()
            serializer = OrderSerializer(model, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = OrderSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CustomerView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = Customer.objects.get(pk=pk)
        except Exception:
            return NotFound("Not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = CustomerSerializer(model, many=False)
            return Response(serializer.data)
        else:
            queryset = Customer.objects.all()
            serializer = CustomerSerializer(queryset, many=True)
            return Response(serializer.data)


class OrderProductView(GenericAPIView):
    def get_object(self, pk):
        try:
            model = OrderProduct.objects.get(pk=pk)
        except Exception:
            return NotFound("Not found")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = OrderProductSerializer(model, many=False)
            return Response(serializer.data)
        else:
            model = get_author_all()
            serializer = OrderProductSerializer(model, many=True)
            return Response(serializer.data)
