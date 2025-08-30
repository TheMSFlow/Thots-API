from rest_framework import serializers, viewsets, permissions, status

from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return (
            Like.objects.all()
            .select_related("user", "post")
            .order_by("-created_at")
        )

    def perform_create(self, serializer):
        post = serializer.validated_data["post"]
        user = self.request.user

        # Check if this user already liked the post
        existing_like = Like.objects.filter(user=user, post=post).first()

        if existing_like:
            # User already liked → unlike (delete it)
            existing_like.delete()
            raise serializers.ValidationError("You have unliked this post.")
        else:
            # User hasn’t liked yet → create new like
            serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        """
        Override create so we can return custom response messages.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post = serializer.validated_data["post"]
        user = request.user

        existing_like = Like.objects.filter(user=user, post=post).first()
        if existing_like:
            existing_like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
        else:
            serializer.save(user=user)
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
