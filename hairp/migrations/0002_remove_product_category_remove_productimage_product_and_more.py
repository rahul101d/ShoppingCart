# Generated by Django 4.2.7 on 2023-12-03 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hairp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]