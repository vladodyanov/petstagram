from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, login, logout
from petstagram.accounts.forms import PetstagramUserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from petstagram.accounts.models import Profile


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)




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


class ProfileDetailsView(OwnerRequiredMixin, views.DetailView):
    queryset = Profile.objects\
        .prefetch_related('user') \
        .all()
    template_name = "accounts/details_profile.html"


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ('first_name', 'last_name', 'profile_picture', 'date_of_birth')

    def get_success_url(self):
        return reverse('details profile', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields['date_of_birth'].widget.attrs['type'] = 'date'

        return form


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete_profile.html'
