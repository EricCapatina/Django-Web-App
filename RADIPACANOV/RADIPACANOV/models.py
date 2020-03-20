from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Notes(models.Model):
    title = models.CharField(null=False, max_length=100)
    body = RichTextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=False, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

