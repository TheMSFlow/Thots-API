from rest_framework import serializers
from .models import Follow


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)  # shows username
    following = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Follow._meta.get_field("following").remote_field.model.objects.all())

    class Meta:
        model = Follow
        fields = ["id", "follower", "following", "created_at"]
        read_only_fields = ["id", "created_at", "follower"]
