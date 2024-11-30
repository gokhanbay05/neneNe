from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    nickname = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nickname}: {self.message}"
    
    class Meta:
        ordering = ['-created_at']
