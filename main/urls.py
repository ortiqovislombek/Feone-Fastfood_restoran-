from django.urls import path

from .views import home,menu,about,book,chekout,orders

urlpatterns = [
    path('',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('book/',book,name='book'),
    path('chekout/<int:pk>',chekout,name='chekout'),
    path('orders/',orders,name='orders')
]
