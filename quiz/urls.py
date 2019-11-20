
from django.urls import path
from .views import QuizListView, QuizReviewView, QuizResponsesView

urlpatterns = [
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
    path('review/<uuid:pk>/', QuizReviewView.as_view(), name='quizreview'),
    path('responses/<uuid:pk>/', QuizResponsesView.as_view(), name='quizresponses')
]