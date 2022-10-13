from django.db import models

class ModelQuestion(models.Model):
    question_text = models.TextField(
        max_length=1000,
        unique=True,
        blank=False,
        null=False,
    )
    answer_option_1 = models.CharField(max_length=100)
    answer_option_2 = models.CharField(max_length=100)
    answer_option_3 = models.CharField(max_length=100, blank=True, null=True)
    answer_option_4 = models.CharField(max_length=100, blank=True, null=True)
    answer_options = [
        ("Option 1", "Option 1"),
        ("Option 2", "Option 2"),
        ("Option 3", "Option 3"),
        ("Option 4", "Option 4"),
    ]
    correct_option = models.CharField(
        max_length=10, choices=answer_options, default="Options 1"
    )

    def __str__(self):
        return self.question_text
