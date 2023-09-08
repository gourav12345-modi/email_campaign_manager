from django.db import models

class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  # Initially active

    def __str__(self):
        return self.email

class Campaigns(models.Model):
    Subject = models.CharField(max_length=255)
    preview_text = models.CharField(max_length=255)
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField()

    def __str__(self):
        return self.Subject
