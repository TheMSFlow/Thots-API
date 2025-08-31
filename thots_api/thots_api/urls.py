from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from comments.views import CommentViewSet
from likes.views import LikeViewSet
from follows.views import FollowViewSet
from users.views import UserListView
from .views import home
from users.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    CurrentUserView,
)

# GraphQL
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"likes", LikeViewSet, basename="like")
router.register(r"follows", FollowViewSet, basename="follow")

urlpatterns = [
    path("", home, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # all REST API routes start with /api/
    path("api/users/", UserListView.as_view(), name="user-list"),
    path("api-auth/", include("rest_framework.urls")),
    
    # Auth endpoints (REST)
    path("api/register/", UserRegistrationView.as_view(), name="register"),
    path("api/login/", UserLoginView.as_view(), name="login"),
    path("api/logout/", UserLogoutView.as_view(), name="logout"),
    path("api/me/", CurrentUserView.as_view(), name="current-user"),

    # ✅ New GraphQL endpoint
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
