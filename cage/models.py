from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from uuslug import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICE = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    objects = models.Manager()  # 默认管理器
    published = PublishedManager()  # 自定义

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)

    def get_absolute_url(self):
        return reverse('cage:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])



