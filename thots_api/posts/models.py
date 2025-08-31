from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_mock = models.BooleanField(default=False)  # ✅ new field to identify mock posts

    def __str__(self):
        return f"{self.user.email}: {self.content[:30]}"
