from django import forms
from django.contrib.auth.models import User
from portal.models import Category, Page, UserProfile


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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password",)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("website", "picture",)
