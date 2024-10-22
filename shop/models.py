from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField()

    def __str__(self) -> str:
        return self.title