from django.db import models
from django.contrib.auth import get_user_model


class Document(models.Model):

    user = models.ForeignKey(
        to=get_user_model(),
        related_name="documents",
        on_delete=models.CASCADE,
        null=False,
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to="documents/")
    created_at = models.DateTimeField(auto_now_add=True)
