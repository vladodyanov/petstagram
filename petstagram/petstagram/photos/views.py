from django.shortcuts import render
from django.urls import reverse_lazy

from petstagram.photos.forms import PetPhotoCreateForm, PetPhotoEditForm
from petstagram.photos.models import PetPhoto
from django.views import generic as views


class PetPhotoCreateView(views.CreateView):
    form_class = PetPhotoCreateForm
    template_name = 'photos/create_photo.html'
    queryset = PetPhoto.objects.all() \
        .prefetch_related('pets')

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.object.pk
        })


class PetPhotoDetailsView(views.DetailView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('photolike_set') \
        .prefetch_related('pets')

    template_name = 'photos/details_photo.html'


class PetPhotoEditView(views.UpdateView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related('pets')
    template_name = 'photos/edit_photo.html'
    form_class = PetPhotoEditForm
