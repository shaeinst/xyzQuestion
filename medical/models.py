from django.db import models

# from django.utils import timezone
# import datetime


class Question(models.Model):
    question_text = models.TextField(max_length=500, unique=True, blank=False, null=False,)
    # pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text[:20]

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(max_length=2000, blank=False, null=False )

    def __str__(self):
        return self.answer_text[:100]

