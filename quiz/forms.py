from django import forms
from django.forms.models import inlineformset_factory
from .models import Quiz, Question, QuizResponse, QuestionResponse

QuestionFormSet = inlineformset_factory(
    Quiz, Question, fields=["quiz", "question_text", "notes_for_question"], exclude=[], can_delete=False, extra=6
)

class QuizResponseForm(forms.Form):
    id_number = forms.IntegerField(label='ID number')
    name = forms.CharField(label='Your name', max_length=100)
