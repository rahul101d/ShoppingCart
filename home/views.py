from django.shortcuts import render
from products.models import Product
from home.models import message
# Create your views her
def nav(request):
    context={'products':Product.objects.all()}
    return render(request,'home/index.html',context)

def product_list(request):
    context={'products':Product.objects.all()}
    return render(request,'products/product_list.html',context)

def p_message(request):
    if request.method=='POST':
        firstname=request.POST.get('first')
        email=request.POST.get('email1')
        comment=request.POST.get('message1')
        user_obj=message.objects.create(first=firstname, mail=email, text=comment)
        user_obj.save()
        messages.success(request,"message recievd sucessfully")
    return render(request,'home/contact.html')

   