from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Quiz, QuizResponse, QuestionResponse
from django.forms.models import formset_factory
from .forms import QuestionFormSet, QuizResponseForm, QuestionResponseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError, transaction


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
    
    @transaction.atomic
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

class QuizEditView(LoginRequiredMixin, UpdateView):
    model = Quiz
    template_name = 'quizedit.html'
    fields = ['title', 'directions_and_introductory_text', 'primary_source_text', 'message']

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(QuizEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["question_formset"] = QuestionFormSet(self.request.POST, instance=self.object)
        else:
            context["question_formset"] = QuestionFormSet(instance=self.object)
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

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)

class QuizDeleteView(LoginRequiredMixin, DeleteView):
    model = Quiz
    template_name = 'quizdelete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return super().get_queryset().filter(author = self.request.user)

@transaction.atomic
def take_quiz(request, quiz_id):
    try:
        with transaction.atomic():
            try:
                quiz = Quiz.objects.get(pk=quiz_id)
            except Quiz.DoesNotExist:
                raise Http404("Bad URL to Quiz.")
    
            quiz_response_form = QuizResponseForm()

            num_questions = quiz.question_set.count()
            QuestionResponseFormset = formset_factory(QuestionResponseForm, extra=num_questions)
            questions = quiz.question_set.all()

            if request.method == "GET":
                question_response_formset = QuestionResponseFormset(request.GET or None)
                questions_and_responses = zip(question_response_formset.forms, questions)

                return render(request, 'takequiz.html', {'quiz': quiz, 
                                                        'quiz_response_form': quiz_response_form,
                                                        'question_response_formset': question_response_formset,
                                                        'questions_and_responses': questions_and_responses})
    
            elif request.method == "POST":
                quiz_response_form = QuizResponseForm(request.POST)
                question_response_formset = QuestionResponseFormset(request.POST)

                if quiz_response_form.is_valid() and question_response_formset.is_valid():
                    quiz_response = QuizResponse.objects.create(
                    quiz = quiz, 
                    id_number=quiz_response_form.cleaned_data['id_number'], 
                    name=quiz_response_form.cleaned_data['name']
                    )
                    quiz_response.save()
                    for index, response in enumerate(question_response_formset):
                        question_response = QuestionResponse.objects.create(
                        quiz_response = quiz_response, 
                        question = quiz.question_set.filter()[index],
                        response_text = response.cleaned_data['response_text']
                        )
                        question_response.save()
        
            return render(request, 'quizsubmitted.html', {'quiz': quiz})

    except IntegrityError:
        handle_exception()