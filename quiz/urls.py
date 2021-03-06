
from django.urls import path
from .views import (
    QuizListView,
    QuizReviewView,
    QuizResponsesView,
    QuizResponsesByRespondentView,
    QuizCreateView,
    QuizEditView,
    QuizDeleteView,
    QuizSubmittedView,
    take_quiz,
)

urlpatterns = [
    path('quiz/new/', QuizCreateView.as_view(), name='createnew'),
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
    path('review/<uuid:pk>/', QuizReviewView.as_view(), name='quizreview'),
    path('responses/<uuid:pk>/', QuizResponsesView.as_view(), name='quizresponses'),
    path('respondents/<uuid:pk>/', QuizResponsesByRespondentView.as_view(), name='quizrespondents'),
    path('edit/<uuid:pk>/', QuizEditView.as_view(), name='quizedit'),
    path('delete/<uuid:pk>/', QuizDeleteView.as_view(), name='quizdelete'),
    path('take/<uuid:quiz_id>/', take_quiz, name='quiztake'),
    path('submitted/<uuid:pk>/', QuizSubmittedView.as_view(), name='quizsubmitted'),
]