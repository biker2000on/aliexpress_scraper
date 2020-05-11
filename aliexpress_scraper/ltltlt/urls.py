from django.urls import path, include

from . import views

app_name = 'ltltlt'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('items', views.getItems, name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/prices', views.getPrices, name='item_detail_prices'),
    path('item/create', views.handleCreate, name='item_create'),
    path('item/<int:pk>/delete', views.ItemDelete.as_view(), name='item_delete'),
    path('accounts/signup', views.signup, name='signup'),
]