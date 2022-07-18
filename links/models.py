from django.db import models
from links.managers import ActiveLinkManager
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User =get_user_model()
# Create your models here.
class Link(models.Model):
    target_url  = models.URLField(max_length=200)
    description =models.CharField(max_length=200)
    identifier=models.SlugField( max_length=20, blank=True, unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    objects = models.Manager()

    public = ActiveLinkManager()

    def __str__(self):
        return self.identifier

