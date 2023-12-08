# Generated by Django 4.2.7 on 2023-12-03 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_price'),
        ('accounts', '0003_cart_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.coupon'),
        ),
    ]