from django.conf import settings
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='tasks',)
    content = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.content
