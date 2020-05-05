from django.shortcuts import render
from django.views import generic

from .models import Item

class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        """Return the last five published questions."""
        return Item.objects.order_by('-created_date')[:5]

# class ItemDetailView(generic.DetailView):
#     template_name = 'item_detail.html'
#     def get_queryset(self):
#         """Return prices for item selected."""
#         Item.objects.filter()