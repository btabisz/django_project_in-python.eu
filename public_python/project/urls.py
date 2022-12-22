from django.contrib import admin
from django.urls import path, include
from project.views import UserUpdateView, logout_view, homepage, PasswordsChangeView, register_complete
from project.views import activation_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('shopping-cart/', include('cart_app.urls')),
    path('aviation/', include('aviation_app.urls')),
    path('accounts/activate/complete/', activation_complete, name="activation_complete"),
    path('accounts/register/complete/', register_complete, name="register_complete"),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/update_user/', UserUpdateView.as_view(), name='update_user'),
    path('accounts/password/', PasswordsChangeView.as_view()),
    path('logout/', logout_view, name='logout'),

]
