from django.contrib import admin
from . import models


class AnswerInline(admin.StackedInline):
    model = models.Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question',               {'fields': ['question_text']}),
        # ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [AnswerInline]
    # list_display = ('question_text', 'pub_date')
    list_display = ('question_text', )

admin.site.register(models.Question, QuestionAdmin)
