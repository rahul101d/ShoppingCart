from django.contrib import admin
from django.urls import path,include
from accounts.views import loginform,register,activate_mail,cart,add_to_cart,remove_cart,remove_coupon
from django.contrib.auth import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
     path('loginform/',loginform, name='loginform'),
     path('register/',register, name='register'),
    path('activate/<email_token>/',activate_mail, name='activate_email'),
    path('cart/',cart, name='cart'),
    path('add-to-cart/<uid>/',add_to_cart, name='add_to_cart'),
    path('remove-cart/<cart_item_uid>/',remove_cart, name='remove_cart'),
    path('remove-coupon/<cart_id>/',remove_coupon, name='remove_coupon'),
   

]
''' path('logout',views.logout, name='logout'),
    path('forgetpass/',views.forget, name='forgetpass'),
    path('reset_password/',v.PasswordResetView.as_view(template_name='accounts/email.html')),
    path('reset_password_sent/',v.PasswordResetDoneView.as_view(template_name='accounts/emailsent.html')),
    path('reset/<uidb64>/<token>/',v.PasswordResetConfirmView.as_view(template_name='accounts/forgetpassword.html'),name='password_reset_confirm'),
    path('reset_password_complete/',v.PasswordResetCompleteView.as_view(template_name='accounts/emailcon.html'),name='password_reset_complete'),'''