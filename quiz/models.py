#import uuid
from django.db import models


class Quiz(models.Model):
    class Meta: 
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
