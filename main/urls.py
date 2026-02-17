from django.urls import path

from .views import home,menu,about,book,chekout,orders,search,payment,payment_success,payment_cancel

urlpatterns = [
    path('',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('book/',book,name='book'),
    path('chekout/<int:pk>',chekout,name='chekout'),
    path('orders/',orders,name='orders'),
    path('search/',search,name='search'),
    
    
    path('payment/<int:order_id>/', payment, name='payment'),
    path('payment/success/<int:order_id>/', payment_success, name='payment_success'),
    path('payment/cancel/<int:order_id>/', payment_cancel, name='payment_cancel'),
]
