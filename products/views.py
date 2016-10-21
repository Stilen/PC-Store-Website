from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, "products.html", context)


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "detail.html", context)
