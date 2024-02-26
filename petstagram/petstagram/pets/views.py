from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms


# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect("details pet", username="max", pet_slug=created_pet.slug)
#
#     context = {
#         "pet_form": pet_form,
#     }
#
#     return render(request, "pets/create_pet.html", context)

class CreatePetView(views.CreateView):
    model = Pet
    form_class = PetCreateForm
    template_name = 'pets/create_pet.html'

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'username': 'max', 'pet_slug': self.object.slug})


class PetDetailView(views.DetailView):
    queryset = Pet.objects.all() \
    .prefetch_related('petphoto_set') \
    .prefetch_related('petphoto_set__photolike_set') \
    .prefetch_related('petphoto_set__pets')

    template_name = 'pets/details_pet.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'


class PetEditView(views.UpdateView):
    model = Pet
    form_class = PetEditForm
    template_name = 'pets/edit_pet.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy('details pet', kwargs={'username': 'max', 'pet_slug': self.object.slug})


class PetDeleteView(views.DeleteView):
    model = Pet
    form_class = PetDeleteForm
    template_name = 'pets/delete_pet.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    success_url = reverse_lazy('index')

    extra_context = {
        'username': 'max',
    }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     form = self.form_class(instance=self.object)
    #     context['form'] = form
    #
    #     return context






# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug) \
#         .get()
#
#     pet_form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         if pet_form.is_valid():
#             pet_form.save()
#             return redirect("details pet", username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/edit_pet.html", context)


# def details_pet(request, username, pet_slug):
#     context = {
#         "pet": Pet.objects.get(slug=pet_slug),
#     }
#
#     return render(request, "pets/details_pet.html", context)


# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         pet_form.save()
#         return redirect("index")
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/delete_pet.html", context)
