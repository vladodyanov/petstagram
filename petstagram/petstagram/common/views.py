from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect

from petstagram.common.models import PhotoLike

from django.views import generic as views


from petstagram.photos.models import PetPhoto


class IndexView(views.ListView):
    # send_mail(
    #     subject="It works!",
    #     message="It works without HTML",
    #     from_email="doncho@ambitioned.com",
    #     recipient_list=["jojobod584@centerf.com"],
    #     html_message="<h1>It works with HTML!</h1>",
    #     fail_silently=False,
    # )
    queryset = PetPhoto.objects.all() \
        .order_by("-created_at") \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set")

    template_name = "common/index.html"

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get("pet_name_pattern", None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["pet_name_pattern"] = self.pet_name_pattern or ""
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query['pets__name__icontains'] = pet_name_pattern

        return queryset.filter(**filter_query)


def like_pet_photo(request, pk):
    pet_photo_like = PhotoLike.objects \
        .filter(pet_photo_id=pk) \
        .first()

    if pet_photo_like:
        # dislike
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")