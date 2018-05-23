from django.urls import path, re_path
from .views import ProductListView


app_name = 'catalog'
urlpatterns = [
    path('', ProductListView.as_view(), name='root'),
    # path('category/<slug:slug>/', ProductListView.as_view(), name='catalog-category'),
    # path('category/<str:region>/<slug:slug>/', ProductListView.as_view(), name='catalog-category-aux'),
    # re_path(r'^manufacturer/(?P<pk>\d+)/$', ManufacturerDetailView.as_view(), name='catalog-manufacturer'),
    # path('product/<slug:slug>/', ProductDetailView.as_view(), name='catalog-product'),
]
