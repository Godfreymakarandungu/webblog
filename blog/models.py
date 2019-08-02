from django.db import models
from datetime import datetime

class Blog(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  urls = models.TextField(default="www.makarablog.duckdns.org")
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
  class Meta:
    verbose_name_plural = "Blog"