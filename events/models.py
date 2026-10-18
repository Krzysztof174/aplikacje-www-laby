from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category name")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="Slug (URL)")
    description = models.TextField(blank=True, verbose_name="Category description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Event title")
    slug = models.SlugField(max_length=220, unique=True, verbose_name="Slug (URL)")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="events",
        verbose_name="Category"
    )
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organized_events",
        verbose_name="Organizer"
    )
    description = models.TextField(verbose_name="Detailed description")
    location = models.CharField(max_length=255, verbose_name="Venue / Address / Online link")
    date = models.DateTimeField(verbose_name="Start date and time")
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Maximum number of attendees"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(0.00)],
        verbose_name="Ticket price (PLN)"
    )
    is_published = models.BooleanField(default=True, verbose_name="Published")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last updated")

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['date']

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d %H:%M')})"
