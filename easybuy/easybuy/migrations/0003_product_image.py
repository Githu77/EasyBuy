# Generated by Django 5.1.2 on 2024-11-11 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easybuy', '0002_cart_order_product_orderitem_cartitem_review_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
