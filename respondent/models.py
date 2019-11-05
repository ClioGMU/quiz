#import uuid
from django.db import models

class Respondent(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(
        'quiz.Quiz',
        on_delete=models.CASCADE,
    )
    id_number = models.IntegerField()


#    def __str__(self):
#        return self.question_text[:50]