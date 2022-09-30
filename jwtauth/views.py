from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from jwtauth import exceptions
from jwtauth.models import ProductModel
from jwtauth.serializers import ProductSerializer, UserSerializer

# Create your views here.


class SignUp(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, **kwargs):
        user = User.objects.filter(username=request.data['email'].lower()).first()
        if user and user.is_active:
            raise exceptions.UseralreadyExists('email')

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class Signin(generics.CreateAPIView):
    def post(self, request, **kwargs):
        user = authenticate(username=request.data['username'].lower(), password=request.data['password'])
        if not user:
            raise exceptions.InvalidUser()
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class ProductView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
