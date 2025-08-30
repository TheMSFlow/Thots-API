from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"likes", LikeViewSet, basename="like")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # all API routes start with /api/
    path("api-auth/", include("rest_framework.urls")),
]
