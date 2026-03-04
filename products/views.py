from django.shortcuts import render, get_object_or_404
from .models import Product

# Home Page
def home_view(request):
    featured_products = Product.objects.filter(is_available=True)[:6]
    return render(request, 'products/home.html', {
        'featured_products': featured_products,
    })


# Product List page
def product_list_view(request):
    product_type = request.GET.get('type')
    products = Product.objects.filter(is_available=True)

    type_titles = {
        'music': 'Music',
        'preset': 'Preset Packs',
        'tuition': 'Tuition',
    }

    if product_type in type_titles:
        products = products.filter(product_type=product_type)
        page_title = type_titles[product_type]
    else:
        page_title = 'All Products'

    return render(request, 'products/product_list.html', {
        'products': products,
        'page_title': page_title,
    })


# Product Detail page
def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'products/product_detail.html', {
        'product': product,
    })