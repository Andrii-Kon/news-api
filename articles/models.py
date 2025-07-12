# articles/models.py

from django.db import models

class Article(models.Model):
    """
    Represents a news article with its title, URL, and summary.
    """
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=500, unique=True)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] # Сортуємо статті за замовчуванням від новіших до старіших