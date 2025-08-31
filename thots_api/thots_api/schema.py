import graphene
from graphene_django import DjangoObjectType
from posts.models import Post
from comments.models import Comment
from likes.models import Like
from users.models import User


# GraphQL Types
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")

    # Override to make username optional
    username = graphene.String(required=False)


class CommentType(DjangoObjectType):
    comment = graphene.String()  # Supabase used "comment" instead of "content"

    class Meta:
        model = Comment
        fields = ("id", "content", "post", "user", "created_at")

    def resolve_comment(root, info):
        return root.content


class LikeType(DjangoObjectType):
    class Meta:
        model = Like
        fields = ("id", "post", "user")


class PostType(DjangoObjectType):
    # Supabase-style fields
    likes = graphene.List(LikeType)
    comments = graphene.List(CommentType)
    likes_count = graphene.Int(name="likesCount")
    comments_count = graphene.Int(name="commentsCount")
    created_at = graphene.DateTime(name="createdAt")  # alias for frontend’s createdAt

    class Meta:
        model = Post
        fields = ("id", "content", "created_at", "user")

    def resolve_likes(root, info):
        return Like.objects.filter(post=root)

    def resolve_comments(root, info):
        return Comment.objects.filter(post=root).order_by("-created_at")

    def resolve_likes_count(root, info):
        return Like.objects.filter(post=root).count()

    def resolve_comments_count(root, info):
        return Comment.objects.filter(post=root).count()


# Queries
class Query(graphene.ObjectType):
    posts = graphene.List(PostType)  # frontend expects "posts"
    post = graphene.Field(PostType, id=graphene.ID(required=True))  # frontend expects "post"

    def resolve_posts(root, info):
        return Post.objects.all().order_by("-created_at")

    def resolve_post(root, info, id):
        return Post.objects.get(id=id)


# Mutations
class CreateComment(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)
        comment = graphene.String(required=True)

    comment_obj = graphene.Field(CommentType)

    @classmethod
    def mutate(cls, root, info, post_id, comment):
        user = info.context.user if info.context.user.is_authenticated else None
        comment_obj = Comment.objects.create(post_id=post_id, content=comment, user=user)
        return CreateComment(comment_obj=comment_obj)


class CreateLike(graphene.Mutation):
    class Arguments:
        post_id = graphene.ID(required=True)

    like = graphene.Field(LikeType)

    @classmethod
    def mutate(cls, root, info, post_id):
        user = info.context.user if info.context.user.is_authenticated else None
        like, _ = Like.objects.get_or_create(post_id=post_id, user=user)
        return CreateLike(like=like)


class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
    create_like = CreateLike.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
