from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('product_details/<str:product_idx>', views.product_details, name='product_details'),
    path('logout/', views.logout, name='logout'),
    path('merchandise/', views.merchandise, name='merchandise'),
]