from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        (0, 'Draft'),
        (1, 'published')
    )

    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_modified']

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_added']


class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField('Post', related_name='categories')
    description = models.TextField(blank=True, default='')
    is_enable = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'categories'

