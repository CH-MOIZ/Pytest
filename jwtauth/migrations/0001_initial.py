# Generated by Django 4.1.1 on 2022-09-22 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('product_category', models.CharField(max_length=128, null=True)),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
