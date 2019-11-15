from django.urls import path

from .views import QuizListView 

urlpatterns = [
    path('dashboard/', QuizListView.as_view(), name='dashboard'),
]