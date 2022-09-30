from django.urls import reverse


def test_get_product(user_factory, product_factory, authed_token_client_generator):
    user = user_factory()
    product = product_factory()
    data = {
        "product_name": "update_product",
        "product_category": "update_category",
        "product_price": 205
    }
    client = authed_token_client_generator(user)
    response = client.patch(reverse('product-details', kwargs={'pk': product.id}), data=data, format='json')
    assert response.json()['product_name'] == data['product_name']
    assert response.json()['id'] == product.id
