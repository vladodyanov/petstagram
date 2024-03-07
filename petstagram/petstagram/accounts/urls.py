from django.urls import path, include

from petstagram.accounts.views import \
    signin_user, \
    details_profile, delete_profile, \
    edit_profile, signout_user, SignupUserView

urlpatterns = (
    path("signup/", SignupUserView.as_view(), name="signup user"),
    path("signin/", signin_user, name="signin user"),
    path("signout/", signout_user, name="signout user"),

    path(
        "profile/<int:pk>/", include([
            path("", details_profile, name="details profile"),
            path("edit/", edit_profile, name="edit profile"),
            path("delete/", delete_profile, name="delete profile")
        ]),
    )
)