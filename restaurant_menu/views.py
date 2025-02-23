from django.shortcuts import render
from .models import Item
from django.views import generic

class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"