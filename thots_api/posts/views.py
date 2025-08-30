from rest_framework import viewsets, permissions
from django.db.models import Count
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            Post.objects.all()
            .select_related("user")              # avoids extra query for user
            .annotate(
                likes_count=Count("likes"),      # pre-count likes
                comments_count=Count("comments") # pre-count comments
            )
            .order_by("-created_at")
        )

    def perform_create(self, serializer):
        # Automatically set the user making the request as the post author
        serializer.save(user=self.request.user)
