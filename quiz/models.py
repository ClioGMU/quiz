from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
    )
    date_created = models.DateField(auto_now=True)
    directions_and_introductory_text = models.TextField(max_length=5000)
    primary_source_text = models.TextField(max_length=20000)
    message = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.title
