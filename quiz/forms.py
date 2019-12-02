from django import forms
from django.forms.models import inlineformset_factory
from .models import Quiz, Question, QuizResponse, QuestionResponse

QuestionFormSet = inlineformset_factory(
    Quiz, Question, fields=["quiz", "question_text", "notes_for_question"], exclude=[], can_delete=False, extra=6
)

#class QuizForm(forms.Form):
    #name = forms.CharField(label='Your name', max_length=100)
    #id_number = models.IntegerField(label='ID number')

class QuizForm(forms.ModelForm):

    class Meta:
        model = QuizResponse
        fields = ('name', 'id_number')
    
    #def process(self):
        #cd = self.cleaned_data

#ResponseFormSet = inlineformset_factory(
    #QuizResponse, QuestionResponse, fields=["response_text"], exclude=[], can_delete=False,
#)