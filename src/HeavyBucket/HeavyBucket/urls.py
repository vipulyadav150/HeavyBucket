

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import url , include
from django.contrib import admin

# from products.views import (
#         ProductListView,
#         product_list_view,
#         ProductDetailView,
#         ProductDetailSlugView,
#         product_detail_view,
#         ProductFeaturedListView,
#         ProductFeaturedDetailView
#         )
from accounts.views import login_page , register_page
from .views import home_page, about_page, contact_page

urlpatterns = [
    url(r'^$', home_page , name='home'),
    url(r'^about/$', about_page  ,name='about'),
    url(r'^contact/$', contact_page , name='contact'),
    url(r'^login/$', login_page ,name='login'),

    url(r'^register/$', register_page ,name='register'),
    url(r'^products/', include('products.urls',namespace='products')),
    url(r'^cart/', include('carts.urls',namespace='cart')),
    url(r'^search/', include('search.urls',namespace='search')),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    # url(r'^products/$', ProductListView.as_view()),
    # url(r'^products-fbv/$', product_list_view),
    # #url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
