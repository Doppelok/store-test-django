from django.urls import path
from . import views

app_name = 'test'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('shop/', views.ShopCategoryView.as_view(), name='shop_category'),
    path('shop/category/<int:category_id>/', views.ShopGroupsView.as_view(), name='shop_groups'),
    path('products/<int:group_id>/', views.ShopProductsView.as_view(), name='shop_products'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/<str:name>/', views.SearchView.as_view(), name='search'),
]
