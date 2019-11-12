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

class Question(models.Model):
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
    )
    question_text = models.TextField(max_length=2000)
    notes_for_question = models.TextField(max_length=2000, blank=True)
    

    def __str__(self):
        return self.question_text[:50]

class Respondent(models.Model):
    id_number = models.IntegerField()
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name[:50]

class QuizResponse(models.Model):
    respondent = models.ForeignKey(
        'Respondent',
        on_delete=models.CASCADE,
    )
    attempt_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.respondent[:50]

class QuestionResponse(models.Model):
    quiz_response = models.ForeignKey(
        'QuizResponse',
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )
    response_text = models.TextField(max_length=2000)

    def __str__(self):
        return self.response_text[:50]
