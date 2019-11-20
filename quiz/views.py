from django.views.generic import ListView, DetailView
from .models import Quiz
from django.contrib.auth.mixins import LoginRequiredMixin

class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz
    template_name = 'dashboard.html'
    ordering = ['-date_created']

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)


class QuizReviewView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quizreview.html'

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)

class QuizResponsesView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quizresponses.html'

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)

class QuizResponsesByRespondentView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quizrespondents.html'

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)