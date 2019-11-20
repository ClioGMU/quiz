
from django.urls import path
from .views import QuizListView, QuizReviewView

urlpatterns = [
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
    path('review/<uuid:pk>/', QuizReviewView.as_view(), name='quizreview'),
]