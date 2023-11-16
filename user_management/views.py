from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets
from django.utils import timezone
from user_management.models import UserModel, StatusChoices
from user_management.serializer import UserSerializer


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     except User.DoesNotExist:  # noqa
#         return Response({'error': 'User not found'}, status=404)
#
#
# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         "refresh": str(refresh),
#         "access": str(refresh.access_token)
#     }


# class SellerView(viewsets.ModelViewSet):
#
#     serializer_class = SellerSerializer
#     queryset = SellerModel.objects.all()


class UserView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = StatusChoices.DELETED
        instance.deleted_at = timezone.now()
        instance.save()
        return Response({"message": "Successful"}, status=200)
