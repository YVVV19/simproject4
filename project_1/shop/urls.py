from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('add_product', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product/<int:product_id>/', views.product_page, name='product_page'),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
