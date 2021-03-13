from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    """
    Linking links to categories and publishing information
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    link = models.URLField(unique=True)
    category = models.ForeignKey('directory.Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)
    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='links_public')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='links_author')
