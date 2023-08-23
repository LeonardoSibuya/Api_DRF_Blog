from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=400, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.title