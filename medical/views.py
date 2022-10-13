from django.shortcuts import render
from django.views.generic import ListView
from .models import Question, Answer


class IndexView(ListView):
    template_name = "medical/index.html"
    context_object_name = "get_question"  # need to change

    def get_queryset(self):
        question = Question.objects.order_by("?").first()
        answer = Answer.objects.get(pk=question.pk)
        context = {
            "question": question,
            "answer": answer,
        }
        return context
