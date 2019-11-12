from django.db import models

class Respondent(models.Model):
    id_number = models.IntegerField()


#    def __str__(self):
#        return self.question_text[:50]