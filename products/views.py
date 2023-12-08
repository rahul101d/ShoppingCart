from django.shortcuts import render
from products.models import Product,Category
from django.http import HttpResponseRedirect
# Create your views here.

def get_product(request,slug):
    try:
        product=Product.objects.get(slug=slug)
        return render(request,'products/product.html',context={'product':product})
    except Exception as e:
        print(e)
    

def get_category(request,slug):
    try:
        category=Category.objects.get(slug=slug)
        return render(request,'products/category.html',context={'category':category})
    except Exception as e:
        print(e)


