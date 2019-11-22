
from django.urls import path
from .views import QuizListView, QuizReviewView, QuizResponsesView, QuizResponsesByRespondentView, QuizCreateView

urlpatterns = [
    path('quiz/new/', QuizCreateView.as_view(), name='createnew'),
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
    path('review/<uuid:pk>/', QuizReviewView.as_view(), name='quizreview'),
    path('responses/<uuid:pk>/', QuizResponsesView.as_view(), name='quizresponses'),
    path('respondents/<uuid:pk>/', QuizResponsesByRespondentView.as_view(), name='quizrespondents'),
]