from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from jwtauth.views import ProductView, Signin, SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('product/', ProductView.as_view(), name='product'),
    path('product/<pk>', ProductView.as_view(), name='product-details'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]