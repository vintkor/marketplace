from .models import Product, ProductVariant
from django.views.generic import ListView


class ProductListView(ListView):
    context_object_name = 'products'
    template_name = 'catalog/product-list.html'

    def get_queryset(self):
        return ProductVariant.objects.select_related(
            'product',
            'product__currency',
            'product__vendor',
        ).filter(is_main=True)
