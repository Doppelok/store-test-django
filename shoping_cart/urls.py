from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'shoping_cart'

urlpatterns = [
    path('cart/', login_required(views.CartView.as_view()), name='cart'),
    path('checkout/', login_required(views.CheckOutView.as_view()), name='checkout'),
    path('cart/add/<int:product_id>', views.add_to_basket, name='add_to_cart'),
    path('cart/remove/<int:product_id>', views.del_from_basket, name='del_from_basket'),
    path('cart/delete/<int:basket_id>', views.remove_basket, name='remove_basket'),
    path('likes/', login_required(views.LikesView.as_view()), name='likes'),
    path('likes/add/<int:product_id>', views.add_to_likes, name='add_to_likes'),
    path('likes/delete/<int:product_id>', views.del_from_likes, name='del_from_likes'),
    path('checkout/success/', login_required(views.SuccessView.as_view()), name='success_view'),
    path('checkout/cancel/', login_required(views.CancelView.as_view()), name='cancel_view'),
    path('checkouts/', login_required(views.CheckoutsListView.as_view()), name='checkouts_list'),
    path('checkouts/order_detail/<int:pk>', login_required(views.OrderDetailView.as_view()), name='order_detail'),
    path('checkout/purchase/', views.stripe_webhook),
    ]
