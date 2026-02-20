from django.urls import path

from goods import views

app_name='goods'

urlpatterns = [
   
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('products/<slug:product_slug>/',views.products, name='products'),
]
