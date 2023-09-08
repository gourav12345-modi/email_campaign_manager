from django.urls import path
from . import views

urlpatterns = [
    path('unsubscribe/<str:email>/', views.unsubscribe_user, name='unsubscribe_user'),
]
