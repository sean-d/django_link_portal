from django.shortcuts import redirect, render, reverse
from .models import Category, Page
from .forms import CategoryForm, PageForm


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


def portal_add_category(request):
    form = CategoryForm()

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect("/portal/")
        else:
            print(form.errors)
    return render(request, "portal/add_category.html", {"form": form})


def portal_add_page(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        category = None

    if category is None:
        return redirect('/portal/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.save()
                return redirect(reverse('portal:portal_show_category',
                                        kwargs={'slug': slug}))
    else:
        print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'portal/add_page.html', context=context_dict)
