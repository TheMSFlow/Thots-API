from rest_framework import serializers
from .models import Post
from comments.models import Comment
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # shows the username
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "user", "content", "created_at", "likes_count", "comments_count"]
        read_only_fields = ["id", "created_at", "likes_count", "comments_count"]

    def get_likes_count(self, obj):
        return Like.objects.filter(post=obj).count()

    def get_comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()
