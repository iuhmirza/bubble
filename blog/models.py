from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Blog(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    
