from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    """
    Links
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    link = models.URLField(unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)


class CategoryLink(models.Model):
    """
    Linking links to categories and publishing information
    """
    link = models.ForeignKey(Link, on_delete=models.PROTECT, related_name='links')
    category = models.ForeignKey('directory.Category', on_delete=models.PROTECT)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
