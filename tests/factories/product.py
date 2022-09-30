import factory
from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory
from pytest_factoryboy import register

faker = FakerFactory.create()


@register
class ProductFactory(DjangoModelFactory):
    product_name = factory.Sequence(lambda x: 'product_name{}'.format(x))
    product_category = factory.Sequence(lambda x: 'product_category{}'.format(x))
    product_price = factory.Sequence(lambda x: x)

    class Meta:
        model = 'jwtauth.ProductModel'
