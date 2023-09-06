from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "network"

urlpatterns = [
    path("", views.index, name="index"),
    path("post-comment/<str:action>", views.post_comment, name="post-comment"),
    path("edit_post/<int:post_Id>", views.edit_post, name="edit_post"),
    path("edit_comment/<int:comment_Id>", views.edit_comment, name="edit_comment"),
    path("delete_post/<int:post_Id>", views.delete_post, name="delete_post"),
    path("delete_comment/<int:comment_Id>", views.delete_comment, name="delete_comment"),
    path("user-profile/<int:user_id>", views.user_profile, name="user-profile"),
    path("edit-profile", views.edit_profile, name="edit-profile"),
    path("following", views.following, name="following"),
    path("follow-unfollow/<int:user_id>", views.follow_unfollow, name="follow-unfollow"),
    path("like/<str:action>/<int:action_id>", views.like, name="like"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
