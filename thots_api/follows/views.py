from rest_framework import viewsets, permissions, status, serializers
from rest_framework.response import Response
from .models import Follow
from .serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Show all follow relationships.
        Each follow object is (follower → following).
        """
        return (
            Follow.objects.all()
            .select_related("follower", "following")
            .order_by("-created_at")
        )

    def perform_create(self, serializer):
        follower = self.request.user
        following = serializer.validated_data["following"]

        if follower == following:
            raise serializers.ValidationError("You cannot follow yourself.")

        # Check if the follow relationship already exists
        existing_follow = Follow.objects.filter(
            follower=follower, following=following
        ).first()

        if existing_follow:
            # Already following → unfollow
            existing_follow.delete()
            raise serializers.ValidationError("You have unfollowed this user.")
        else:
            # Not following yet → create new follow
            serializer.save(follower=follower)

    def create(self, request, *args, **kwargs):
        """
        Override create so we can return custom response messages.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        follower = request.user
        following = serializer.validated_data["following"]

        if follower == following:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        existing_follow = Follow.objects.filter(
            follower=follower, following=following
        ).first()

        if existing_follow:
            existing_follow.delete()
            return Response(
                {"detail": "User unfollowed."}, status=status.HTTP_200_OK
            )
        else:
            serializer.save(follower=follower)
            return Response(
                {"detail": "User followed."}, status=status.HTTP_201_CREATED
            )
