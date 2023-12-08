"""
URL configuration for shoppingcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from hairp import views
from django.contrib.auth import views as v

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('nav/',include('home.urls')),
    
    path('product/',include('products.urls')),
    path('admin/', admin.site.urls),
    path('ipaddress/',views.ipaddress,name='ipaddress'),
    path('hom/',views.home, name='home'),
    path('logout',views.logout, name='logout'),
   ]
''' path('form',views.userform, name='form'),
    path('accounts/',include('django.contrib.auth.urls')),
    
    path('forgetpass/',views.forget, name='forgetpass'),
    path('reset_password/',v.PasswordResetView.as_view(template_name='hairp/email.html')),
    path('reset_password_sent/',v.PasswordResetDoneView.as_view(template_name='hairp/emailsent.html')),
    path('reset/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='hairp/forgetpassword.html'),name='password_reset_confirm'),
    path('reset_password_complete/',v.PasswordResetCompleteView.as_view(template_name='hairp/emailcon.html'),name='password_reset_complete'),
'''

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()