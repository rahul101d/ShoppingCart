from django.contrib import admin
from django.urls import path,include
from home import views
from django.contrib.auth import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.nav, name='nav'),
    path('contact/',views.p_message, name='p_message'),
    path('product_list/',views.product_list, name='product_list'),
     
]