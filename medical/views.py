from django.views.generic import ListView
from .models import ModelQuestion


class IndexView(ListView):
    template_name = "medical/index.html"
    context_object_name = "get_model"

    def get_queryset(self):
        model_question = ModelQuestion.objects.order_by("?").first()
        correct_option = model_question.correct_option

        answer_option_1 = model_question.answer_option_1
        answer_option_2 = model_question.answer_option_2
        answer_option_3 = model_question.answer_option_3
        answer_option_4 = model_question.answer_option_4

        option = "A"
        correct_answer = answer_option_1

        if correct_option == "Option 2":
            correct_answer = answer_option_2
            option = "B"
        if correct_option == "Option 3":
            correct_answer = answer_option_3
            option = "C"
        if correct_option == "Option 4":
            correct_answer = answer_option_4
            option = "D"

        context = {
            "question": model_question,
            "correct_answer": correct_answer,
            "option": option,
            "option_1": answer_option_1,
            "option_2": answer_option_2,
            "option_3": answer_option_3,
            "option_4": answer_option_4,
        }
        return context
