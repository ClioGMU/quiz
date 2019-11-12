from django.contrib import admin
from .models import Quiz
from .models import Question
from .models import Respondent
from .models import QuizResponse
from .models import QuestionResponse

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Respondent)
admin.site.register(QuizResponse)
admin.site.register(QuestionResponse)