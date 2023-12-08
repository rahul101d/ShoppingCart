from django.shortcuts import render,redirect,HttpResponse

from django.contrib.auth.models import User
from hairp.form import sig,sig1,sig2
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.contrib.auth.views import PasswordResetView
from django.conf import settings


# Create your views here.

    
def logout(request):
    auth.logout(request)
    return redirect('/nav/home')


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
                return redirect('/nav/home')
    return render (request,'hairp/forgetpassword.html')

def ipaddress(request):
    user_ip= request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None: 
        ip=user_ip.split(',')
    else:
        ip=request.META.get('REMOTE_ADDR')
    return render(request,'hairp/ipaddress.html',{'ip':ip})



def home(request):
    return render(request,'hairp/home.html')

def emailver(request):
    return render(request,'hairp/email.html')

def mail_sent(request):
    return render(request,'hairp/emailsent.html')

def emailcon(request):
    return render(request,'hairp/emailcon.html')