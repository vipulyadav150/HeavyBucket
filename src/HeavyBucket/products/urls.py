
from django.conf.urls import url , include


from .views import (
        ProductListView,
        # product_list_view,
        # ProductDetailView,
        ProductDetailSlugView,
        # product_detail_view,
        # ProductFeaturedListView,
        # ProductFeaturedDetailView
        )


app_name = 'products'

urlpatterns = [


    url(r'^$', ProductListView.as_view(),name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(),name = 'detail'),

]


