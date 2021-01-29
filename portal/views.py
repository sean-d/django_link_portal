from django.shortcuts import render
from .models import Category


def portal_index(request):
    category_list = Category.objects.order_by("-likes")
    context = {"boldmessage": "why hello there", "category_list": category_list}
    return render(request, "portal/index.html", context=context)


def portal_about(request):
    return render(request, "portal/about.html", {"aboutmessage": "welcome to about page."})
