from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('index/', views.index, name='index'),
    # path('api/get_user_notifications/', views.get_user_notifications, name='get user notifications')
]
