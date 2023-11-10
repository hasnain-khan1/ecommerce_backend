from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Category, Product, Cart, CartItem, Checkout, BuyProduct
from .serializers import (CategorySerializer, ProductSerializer, CheckoutSerializer, CartSerializer, CartItemSerializer,
                          BuyProductSerializer)
from user_management.models import StatusChoices


class CategoryView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class ProductView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200

        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def seller_products(self, request):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            seller = self.request.user.id
            seller_product = self.get_queryset().filter(seller_id=seller)
            serialized_data = self.get_serializer(seller_product, many=True)
            return Response({'data': serialized_data.data, "message": "Successful"})
        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class CartView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class CheckoutView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class CartItemView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class BuyProductView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializer

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE, checkout__user=request.user)
            serialized_data = self.get_serializer(data, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            msg = f"Exception in Category -> {er}"
            return_response['message'] = msg
            status = 400
        finally:
            return Response(return_response, status=status)

    def create(self, request, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            if serialized_data := self.get_serializer(data=request.data):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(pk=pk, status=StatusChoices.ACTIVE)
            serialized_data = self.get_serializer(data).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400
        finally:
            return Response(return_response, status=status)

    def update(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            queryset = self.get_queryset().filter(pk=pk)
            if serialized_data := self.get_serializer(queryset, data=request.data, partial=True):
                serialized_data.save()
                return_response['data'] = serialized_data.data

            else:
                return_response['message'] = f"Bad Request -> {serialized_data.errors}"
                status = 400

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)
