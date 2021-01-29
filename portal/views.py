from django.shortcuts import render
from .models import Category, Page


def portal_index(request):
    category_list = Category.objects.order_by("-likes")
    page_list = Page.objects.order_by("-views")[:5]
    context = {"boldmessage": "why hello there", "category_list": category_list, "page_list": page_list}
    return render(request, "portal/index.html", context=context)


def portal_about(request):
    return render(request, "portal/about.html", {"aboutmessage": "welcome to about page."})


def portal_show_category(request, slug):
    context = {}

    try:
        category = Category.objects.get(slug=slug)
        pages = Page.objects.filter(category=category)
        context["category"] = category
        context["pages"] = pages

    except Category.DoesNotExist:
        context["category"] = None
        context["pages"] = None

    return render(request, "portal/category.html", context=context)
