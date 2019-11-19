from django.urls import path
from django.views.generic import TemplateView
from .views import QuizListView, QuizReviewView

urlpatterns = [
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
    path('quizreview/<uuid:pk>/', QuizReviewView.as_view(), name='quizreview'),
    path('', TemplateView.as_view(template_name="home.html"), name='home')
]