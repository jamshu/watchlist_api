from django.db import models


class Watchlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
