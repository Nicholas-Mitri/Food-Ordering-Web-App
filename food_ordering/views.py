from re import template
from django.shortcuts import render
from django.views import generic
from .models import MEAL_TYPE, Item


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("date_created")
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        print(context.keys())
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"


class AddItem(generic.CreateView):
    pass
