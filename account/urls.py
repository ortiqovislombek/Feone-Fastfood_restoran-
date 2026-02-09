from django.urls import path

from .views import login_view,register_view,logout_view 
from .views import profile_view ,admin_view ,security_view,order_view,create_product,edit_product,delete_product


urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('logout/',logout_view,name='logout'),
    
    path('profil/',profile_view,name='profil'),
    path('order/',order_view,name='order'),
    path('admin/',admin_view,name='admin'),
    path('security/',security_view,name='security'),
    path('create_product/',create_product,name='create_product'),
    path('edit_product/<int:pk>',edit_product,name='edit_product'),
    path('delete_product/<int:pk>',delete_product,name='delete_product'),
]
