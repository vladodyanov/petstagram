from django.urls import path, include

from petstagram.photos.views import PetPhotoCreateView, PetPhotoDetailsView, PetPhotoEditView

urlpatterns = (
    path("create/", PetPhotoCreateView.as_view(), name="create photo"),
    path(
        "<int:pk>/",
        include([
            path("", PetPhotoDetailsView.as_view(), name="details photo"),
            path("edit/", PetPhotoEditView.as_view(), name="edit photo"),
        ]),
    ),
)