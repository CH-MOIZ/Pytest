import pytz
from django.urls import reverse
from django.utils import timezone
from rest_framework import status


def test_get_product(user_factory, product_factory, authed_token_client_generator):
    user = user_factory()
    product = product_factory()
    client = authed_token_client_generator(user)
    response = client.get(reverse('product'))
    assert response.json()[0]['id'] == product.id


def test_create_product(user_factory, authed_token_client_generator, mocker):
    date = timezone.datetime(2022, 5, 1, 11, 0, 0, tzinfo=pytz.timezone('America/New_York'))
    mock_now = mocker.patch('django.utils.timezone.now')
    mock_now.return_value = date
    user = user_factory()
    data ={
     "product_name":"test_product",
     "product_category":"test_Catgory",
     "product_price":200
    }
    client = authed_token_client_generator(user)
    response = client.post(reverse('product'), data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()['product_name'] == data['product_name']

