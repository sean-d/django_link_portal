from django import forms
from portal.models import Category, Page


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="enter a category name")

    class Meta:
        model = Category
        fields = ("name",)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="enter a page title")
    url = forms.URLField(max_length=200, help_text="please enter a valid URL (http:// or https://)")

    class Meta:
        model = Page
        exclude = ("category", "views",)
