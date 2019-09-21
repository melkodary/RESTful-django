from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser
from .serializers import UserSerializer, AuthTokenSerializer
from .models import User
from django.db import IntegrityError


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # request.data['username'] = request.data['phone']
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        serializer = AuthTokenSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'phone': user.phone
            })
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class UserListView(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUsersView(generics.CreateAPIView):
    # permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            _ = serializer.create(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({
                'phone': "phone already exists",
            }, status=status.HTTP_409_CONFLICT)