from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from product.models import Product


def map_view(request):
    context = {
    }
    return render(request, 'map/map.html', context)

# class ProductDetailView(DetailView):
#     model = Product
#
# def detail(request, id):
#     product = Product.objects.get(id = id)
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'product/product_detail.html', {'product' : product})

