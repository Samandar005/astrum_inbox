from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class Message(models.Model):
    from_email = models.EmailField()
    to_email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_detail_url(self):
        return reverse('inbox:detail', args=[self.pk])