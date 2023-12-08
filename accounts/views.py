from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.contrib import messages,auth
from products.models import *

from .models import Profile
from tkinter import E
from math import log
from products.models import Product,Coupon
from accounts.models import Cart,CartItems



# Create your views here.
def form1(request):
    a=sig2()
    return render(request,'accounts/aa.html',{'a':a})
    
def logout(request):
    auth.logout(request)
    return redirect('/home')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request,'Email is already taken.')
            return HttpResponseRedirect(request.path_info)
        user_obj=User.objects.create(first_name=first_name, last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request,"An email has been sent on your mail.")
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/register.html')


   

def loginform(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj=User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request,'Account not found!.')
            return HttpResponseRedirect(request.path_info)
        user_obj=authenticate(username=email,password=password)
        if user_obj:
            login(request,user_obj)
            return redirect('/home')
        
        messages.warning(request,"Envalid credentials.")
        return HttpResponseRedirect(request.path_info)
    return render(request,'accounts/loginform.html')

def activate_mail(request, email_token):
    try:
        user=Profile.objects.get(email_token=email_token)
        user.is_email_verified=True
        user.save()
        return redirect('/nav/home')
    except Exception as e:
        return HttpResponse('Invalid Email')

def forget(request):
    a=request.POST.get('username')
    form=sig1(a,request.POST)
    x=request.POST.get('new_password1')
    if request.method=='POST':
        if User.objects.filter(username=a):
            form=sig1(a,request.POST)
            if form.is_valid():
                u=User.objects.get(username=a)
                u.set_password(x)
                u.save()
                return redirect('/home')
    return render (request,'accounts/forgetpassword.html')

def ipaddress(request):
    user_ip= request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None: 
        ip=user_ip.split(',')
    else:
        ip=request.META.get('REMOTE_ADDR')
    return render(request,'accounts/ipaddress.html',{'ip':ip})

def emailver(request):
    return render(request,'accounts/email.html')

def mail_sent(request):
    return render(request,'accounts/emailsent.html')

def emailcon(request):
    return render(request,'accounts/emailcon.html')


def add_to_cart(request,uid):
    product=Product.objects.get(uid=uid)
    user=request.user
    cart,_=Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item=CartItems.objects.create(cart=cart,product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        

    

def cart(request):
    cart_obj=Cart.objects.get(is_paid=False,user=request.user)
    if request.method=='POST':
        coupon=request.POST.get('coupon')
        coupon_obj=Coupon.objects.filter(coupon_code__icontains=coupon)
        if not coupon_obj.exists():
            messages.warning(request,'Invalid Coupon')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart_obj.coupon:
            messages.warning(request,'Coupon already exists')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart_obj.get_cart_total()<coupon_obj[0].minimum_amount:
            messages.warning(request,f'Amount should be greater than {coupon_obj[0].minimum_amount}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if cart_obj[0].is_expired:
            messages.warning(request,f'coupon expired')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        cart_obj.coupon=coupon_obj[0]
        cart_obj.save()
        messages.success(request,'Coupon applied')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    context={'cart':cart_obj}
    return render(request,'accounts/cart.html',context)

def remove_coupon(request,cart_id):
    cart=Cart.objects.get(uid=cart_id)
    cart.coupon=None
    cart.save()
    messages.success(request,'Coupon removed')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def remove_cart(request,cart_item_uid):
    try:
        cart_item=CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
