from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from goods.models import Products
from goods.utils import q_search

def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by',None)
    query=request.GET.get('q', None)

    if category_slug == "vse-tovary":
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))
    
    if on_sale:
        goods=goods.filter(discount__gt=0)
    if order_by and order_by !="default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    curr_page=paginator.page(int(page))
    
    
    context={
        'title':'Motolab',
        'goods':curr_page,
        'slug_url':category_slug
            
    } 

    return render(request, 'goods/catalog.html', context)

def products(request, product_slug):

    product=Products.objects.get(slug=product_slug)

    context={'product': product}
    return render(request, 'goods/products.html', context)