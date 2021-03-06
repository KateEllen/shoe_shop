from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_date_posted = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, default="", blank=True,
                                    on_delete=models.CASCADE,
                                    related_name='post')

    class Meta:
        ordering = ['-post_date_posted']

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    post_id = models.ForeignKey('Post', null=True,
                                related_name="comments", blank=True,
                                on_delete=models.SET_NULL)
    comment_title = models.CharField(max_length=50)
    comment_content = models.TextField(max_length=500)
    comment_date_posted = models.DateTimeField(default=timezone.now)
    comment_author = models.ForeignKey(User, null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name='comment')

    class Meta:
        ordering = ['-comment_date_posted']

    def __str__(self):
        return self.comment_title
