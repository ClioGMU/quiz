from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Quiz, QuizResponse, QuestionResponse
from .forms import QuestionFormSet, QuizForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


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

class QuizSubmittedView(DetailView):
    model = Quiz
    template_name = 'quizsubmitted.html'

class QuizCreateView(LoginRequiredMixin, CreateView):
    model = Quiz
    template_name = 'createnew.html'
    fields = ['title', 'directions_and_introductory_text', 'primary_source_text', 'message']
    
    def get_context_data(self, **kwargs):
        context = super(QuizCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["question_formset"] = QuestionFormSet(self.request.POST)
        else:
            context["question_formset"] = QuestionFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset = context["question_formset"]
        form.instance.author = self.request.user
        if formset.is_valid():
            response = super().form_valid(form)
            formset.instance = self.object
            formset.save()
            return response
        else:
            return super().form_invalid(form)

def take_quiz(request, quiz_id):
    #form = QuizForm()
    #quiz = Quiz.objects.get(pk=quiz_id)
    if request.method == "GET":
        form = QuizForm(request.POST)
        quiz = Quiz.objects.get(pk=quiz_id)
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            raise Http404("Bad URL to Quiz.")
        return render(request, 'takequiz.html', {'quiz': quiz, 'form': form})
    elif request.method == "POST":
        form = QuizForm()
        quiz = Quiz.objects.get(pk=quiz_id)
        if form.is_valid():
            obj = QuizResponse()
            obj.name = form.cleaned_data['name']
            obj.id_number = form.cleaned_data['id_number']
            obj.quiz = quiz
            obj.save()

            #response = super().form_valid(form)
            #forms.instance = self.object
            #form.save()
            #form.process()
            #name = form.cleaned_data['name']
            #id_number = form.cleaned_data['id_number']
            #quiz = quiz_id
        #context = {'form': form }
        
        return render(request, 'quizsubmitted.html', {'quiz': quiz})

        #else:
            #return render(request, 'takequiz.html', {'quiz': quiz, 'form': form})

#return render(request, 'takequiz.html', {'quiz': quiz, 'form': form})
#return render(request, 'quizsubmitted.html', {'quiz': quiz})
#return HttpResponseRedirect(reverse('submitted/<uuid:pk>/'), )