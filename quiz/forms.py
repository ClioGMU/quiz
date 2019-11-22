from django.forms.models import inlineformset_factory
from .models import Quiz, Question

QuestionFormSet = inlineformset_factory(
    Quiz, Question, fields=["quiz", "question_text", "notes_for_question"], exclude=[], can_delete=False
)