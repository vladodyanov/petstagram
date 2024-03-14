from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from petstagram.accounts.forms import PetstagramUserCreationForm
from django.urls import reverse_lazy
from django.views import generic as views


class SignInUserView(auth_views.LoginView):
    template_name = 'accounts/signin_user.html'
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
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
