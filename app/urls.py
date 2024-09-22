from django.urls import path
from app import views

urlpatterns = [
    path('', views.test, name='test'),
    path('send_mail/', views.send_email_to_all_func, name='send_mail'),
]
