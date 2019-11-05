#import uuid
from django.db import models

class Response(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(
        'quiz.Quiz',
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        'question.Question',
        on_delete=models.CASCADE,
    )
    respondent = models.ForeignKey(
        'respondent.Respondent',
        on_delete=models.CASCADE,
    )
    response_text = models.TextField(max_length=2000)


    def __str__(self):
        return self.response_text[:50]
