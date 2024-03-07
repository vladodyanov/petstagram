from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


# Callables:
# - all functions
# - objects with overriden `__call__` method

# def signup_user(request):
#     context = {}
#     return render(request, "accounts/signup_user.html", context)

class SignupUserView(auth_views.LoginView):
    template_name = "accounts/signup_user.html"

    def get_success_url(self):
        return reverse_lazy('index')


def signin_user(request):
    context = {}

    return render(request, "accounts/signin_user.html", context)





def signout_user(request):
    # signout user
    return redirect('index')


def details_profile(request, pk):
    context = {}

    return render(request, "accounts/details_profile.html", context)


def edit_profile(request, pk):
    context = {}

    return render(request, "accounts/edit_profile.html", context)


def delete_profile(request, pk):
    context = {}
    return render(request, "accounts/delete_profile.html", context)
