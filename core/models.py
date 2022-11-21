"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db.models.signals import post_save
from django.dispatch import receiver


def track_image_file_path(instance, filename):
    """Generate file path for new track image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'track', filename)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    USER = 1
    LEADER = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (USER, 'User'),
        (LEADER, 'Leader'),
        (ADMIN, 'Admin'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             unique=True, on_delete=models.CASCADE,)
    nickname = models.CharField(max_length=225)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, null=True, blank=True)
    subjects = models.CharField(max_length=225)
    image_url = models.CharField(max_length=225)
    #followed_tracks = models.ManyToManyField('Track', blank =True)

    def __str__(self):
        return self.user.nickname


class User_Data(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    track_id = models.IntegerField(blank=True)
    follow_date = models.DateTimeField(default=timezone.now)
    track_started = models.BooleanField(default=False)


class Content(models.Model):
    """Content object."""
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        blank=True,
    )
    subject_major = models.CharField(max_length=255)
    subject_minor = models.CharField(max_length=255)
    target_test = models.CharField(max_length=255)
    target_grade = models.CharField(max_length=255)
    content_name = models.CharField(max_length=255)
    book = models.ForeignKey(
        'Book',
        on_delete=models.CASCADE,
        blank=True,
    )
    description = models.TextField(blank=True)
    #link = models.CharField(max_length=255, blank=True)
    #followers = models.ManyToManyField('User', blank =True)
    followers_num = models.IntegerField()
    #comment_track = models.ManyToManyField('Comment_Track', blank=True)
    rating_avg = models.DecimalField(max_digits=5, decimal_places=2)
    #image = models.ImageField(null=True, upload_to=track_image_file_path)
    image_url = models.CharField(max_length=225, blank=True)
    #published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Track(models.Model):
    """Track object."""
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = models.ForeignKey(
        'Content',
        on_delete=models.CASCADE,
        blank=True,
    )
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        blank=True,
    )
    track_name = models.CharField(max_length=225)
    image_url = models.CharField(max_length=225)
    published_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    followers_num = models.IntegerField()
    rating_avg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    track = models.ForeignKey(
        'Track',
        on_delete=models.CASCADE,
        blank=True,
    )
    order_major = models.IntegerField()
    order_minor = models.IntegerField()
    task_name = models.CharField(max_length=255)
    ranges = models.CharField(max_length=255)
    learning_time = models.CharField(max_length=255)
    guideline = models.CharField(max_length=255)
    #comment_task = models.CharField(max_length=255)
    references = models.CharField(max_length=255)


class Content_Star_Point(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content_id = models.IntegerField()
    star_point = models.IntegerField()


class Track_Star_Point(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    track_id = models.IntegerField()
    star_point = models.IntegerField()


class Task_Star_Point(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    task_id = models.IntegerField()
    star_point = models.IntegerField()


class Book(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    published_date = models.DateTimeField(default=timezone.now)


class Track_Completion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    track_id = models.IntegerField()
    task_id = models.IntegerField()
    complete_date = models.DateTimeField(default=timezone.now)


class Comment_Track(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="track_reviews",
    )
    track = models.ForeignKey(
        'Track',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="track_reviews",
    )
    comment = models.TextField()
    rating = models.PositiveIntegerField()

    def __str___(self) -> str:
        return f"{self.user} / {self.rating}"


class Comment_Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="task_reviews",
    )
    task = models.ForeignKey(
        'Task',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="task_reviews",
    )
    comment = models.CharField(max_length=225)


'''class Recipe(models.Model):
    """Recipe object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField('Tag')
    ingredients = models.ManyToManyField('Ingredient')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        return self.title'''
