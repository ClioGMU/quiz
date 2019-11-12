from django.db import models

class Question(models.Model):
    quiz = models.ForeignKey(
        'quiz.Quiz',
        on_delete=models.CASCADE,
    )
    question_text = models.TextField(max_length=2000)
    notes_for_question = models.TextField(max_length=2000, blank=True)
    

    def __str__(self):
        return self.question_text[:50]
