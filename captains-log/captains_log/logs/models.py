from django.db import models


class Log(models.Model):
    star_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)

    class Meta:
        ordering = ["star_date"]
