# api/urls.py
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentViewSet, GroupListView, FollowViewSet

router = SimpleRouter()
router.register("follow", FollowViewSet, basename="follow")
router.register("groups", GroupListView, basename="groups")
router.register("posts", PostViewSet, basename="posts")

urlpatterns = [
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),

    path(
        "v1/posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comments-list",
    ),
    path(
        "v1/posts/<int:post_id>/comments/<int:id>/",
        CommentViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy"
            }
        ),
        name="comments-detail",
    ),
]
