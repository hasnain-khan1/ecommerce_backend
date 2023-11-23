from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import (Category, Product, Cart, CartItem, Checkout, BuyProduct, Review, ProductVariation, ProductAttribute,
                     Sale)
from .serializers import (CategorySerializer, ProductSerializer, CheckoutSerializer, CartSerializer, CartItemSerializer,
                          BuyProductSerializer, ReviewSerializer, ProductVariationSerializer,
                          ProductAttributesSerializer, SaleSerializer)
from user_management.models import StatusChoices
from django.utils import timezone
from .utils.pagination import StandardResultsSetPagination


class CategoryView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class ProductView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)

    def retrieve(self, request, pk=None, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_object()
            serialized_data = self.get_serializer(data).data
            reviews = data.reviews.all()
            reviews_serialized = ReviewSerializer(reviews, many=True).data
            variations = data.variations.all()
            serialized_var = ProductVariationSerializer(variations, many=True).data
            serialized_data['variation'] = serialized_var

            serialized_data['reviews'] = reviews_serialized
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
            queryset = self.paginate_queryset(seller)
            serialized_data = self.get_serializer(queryset, many=True).data
            return Response({'data': serialized_data.data, "message": "Successful"})
        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)

    def search_product(self, request):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            color = self.request.query_params.get('c')
            size = self.request.query_params.get('s')
            category = self.request.query_params.get('cate')
            queryset = ProductVariation.objects.all()
            if all((category, color, size)):
                queryset = (queryset.filter(product__category__id=category, color=color, size=size).
                            values_list('product', flat=True))
            elif all((category, size)):
                queryset = queryset.filter(product__category__id=category, size=size).values_list('product', flat=True)
            elif all((category, color)):
                queryset = queryset.filter(product__category__id=category, color=color).values_list('product', flat=True)
            if word := self.request.query_params.get('w'):
                word_query = Q(product__name__icontains=word) | Q(product__description__icontains=word)
                queryset = queryset.filter(word_query).values_list('product', flat=True)
            queryset = self.get_queryset().filter(id__in=queryset)
            queryset = self.paginate_queryset(queryset)
            serialized_data = self.get_serializer(queryset, many=True).data
            return_response['data'] = serialized_data

        except Exception as er:
            return_response['message'] = f"Exception in Category -> {er}"
            status = 400

        finally:
            return Response(return_response, status=status)


class ProductVariationView(viewsets.ModelViewSet):
    queryset = ProductVariation.objects.all()
    serializer_class = ProductVariationSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class ProductAttributeView(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributesSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)

class ReviewView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class CartView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE, user=1)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class CheckoutView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE, cart__user=1)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class CartItemView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE, cart__user=1)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class BuyProductView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = BuyProduct.objects.all()
    serializer_class = BuyProductSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE, checkout__cart__user=1)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)


class SaleView(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        return_response = {'data': [], 'message': "Successful"}
        status = 200
        try:
            data = self.get_queryset().filter(status=StatusChoices.ACTIVE)
            queryset = self.paginate_queryset(data)
            serialized_data = self.get_serializer(queryset, many=True).data
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
            serialized_data = self.get_serializer(data=request.data)
            if serialized_data.is_valid():
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
            data = self.get_object()
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)
