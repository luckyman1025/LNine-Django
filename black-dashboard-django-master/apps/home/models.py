# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.translation import gettext_lazy as _

# class User(AbstractUser):
#     # ... existing fields ...
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',
#         blank=True,
#         verbose_name=_('groups'),
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_set',
#         blank=True,
#         verbose_name=_('user permissions'),
#         help_text=_('Specific permissions for this user.'),
#     )

#     language = models.CharField(
#         max_length=2,
#         choices=[('en', 'English'), ('es', 'Spanish')],
#         default='en'
#     )

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):

    LANGUAGE_CHOICES = [
        ('en', _('English')),
        ('es', _('Spanish')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    profile = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)
    language = models.CharField(  # Added language field
        max_length=2,
        choices=LANGUAGE_CHOICES,
        default='en',
        verbose_name=_('language')
    )

    class Meta:
        unique_together = ['user', 'company']

    def __str__(self):
        return f"{self.user.username} - {self.company.name}"



