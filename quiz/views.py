from django.views.generic import ListView, DetailView
from .models import Quiz
from django.contrib.auth.mixins import LoginRequiredMixin

class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'dashboard.html'
    ordering = ['-date_created']

class QuizReviewView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quizreview.html'
    ordering = ['-date_created']
