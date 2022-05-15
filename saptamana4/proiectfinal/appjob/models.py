from django.db import models


class Jobs(models.Model):
    tip_job = models.CharField(max_length=11)
    url_job = models.CharField(max_length=100)
    title_job = models.CharField(max_length=100)
    description_job = models.TextField(blank=True)
    how_to_apply = models.TextField(blank=True)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.tip_job} - {self.url_job}"
