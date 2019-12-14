import uuid
from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    class Meta: 
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    
    def get_absolute_url(self):
        return reverse('quizreview', args=[str(self.id)])

class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
    )
    question_text = models.TextField(max_length=2000, blank=True)
    notes_for_question = models.TextField(max_length=2000, blank=True)
    

    def __str__(self):
        return self.quiz.title[:50] + ": " + self.question_text[:50]

class QuizResponse(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
    )
    id_number = models.IntegerField()
    name = models.CharField(max_length=100)
    attempt_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.quiz.title[:50] + ": " + self.name
    
    def get_absolute_url(self):
        return reverse('quizsubmitted', args=[str(self.quiz_id)])

class QuestionResponse(models.Model):
    quiz_response = models.ForeignKey(
        QuizResponse,
        on_delete=models.CASCADE,
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    response_text = models.TextField(max_length=2000, null=True)
 
    def __str__(self):
        return self.quiz_response.quiz.title[:50] + ": " + self.quiz_response.name + " on " + self.question.question_text[:50]
