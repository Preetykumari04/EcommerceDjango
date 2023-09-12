from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('menshirt',views.menshirt,name='menshirt'),
    path('mentshirt',views.mentshirt,name='mentshirt'),
    path('menjeans',views.menjeans,name='menjeans'),
    path('womenjeans',views.womenjeans,name='womenjeans'),
    path('womentop',views.womentop,name='womentop'),
    path('womenkurti',views.womenkurti,name='womenkurti'),
    path('kidboy',views.kidboy,name='kidboy'),
    path('kidgirlsummer',views.kidgirlsummer,name='kidgirlsummer'),
    path('kidgawn',views.kidgawn,name='kidgawn'),
    path('cart',views.cart,name='cart'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signup',views.signup,name='signup'),
    path('regis',views.regis,name='regis'),
    path('loginsuccess',views.loginsuccess,name='loginsuccess'),
    path('edit_user/<id>',views.edit_user,name='edit_user'),
    path('delete_user/<id>',views.delete_user,name='delete_user'),
    path('retrive_user/<id>',views.retrive_user,name='retrive_user'),
    path('update',views.update,name='update'),
    path('logout',views.logout,name='logout'),
    
    path('add_to_cart/<str:product_type>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('qty_less/<int:cart_item_id>/', views.qty_less, name='qty_less'),
    path('qty_up/<int:cart_item_id>/', views.qty_up, name='qty_up'),
    path('del_from_cart/<int:cart_item_id>/', views.del_from_cart, name='del_from_cart'),
    path('cart/', views.cart, name='cart'),  # Add this line for the cart view
    path('buy-now/', views.buy_now, name='buy_now'),
    path('order-history/', views.order_history, name='order_history'),
    
]