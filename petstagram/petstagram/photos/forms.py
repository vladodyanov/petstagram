from django import forms

from petstagram.core.form_mixins import ReadonlyFieldsFormMixin
from petstagram.photos.models import PetPhoto


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ("photo", "description", "location", 'pets')


class PetPhotoCreateForm(PhotoBaseForm):
    pass


class PetPhotoEditForm(ReadonlyFieldsFormMixin, PhotoBaseForm):
    readonly_fields = ("photo",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
