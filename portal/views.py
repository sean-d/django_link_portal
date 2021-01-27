from django.shortcuts import render
from django.http import HttpResponse


def portal_index(request):
    context = {"boldmessage": "why hello there"}
    return render(request, "portal/index.html", context=context)


def portal_about(request):
    return render(request, "portal/about.html", {"aboutmessage": "welcome to about page."})
