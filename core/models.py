from django.db import models


class Riddle(models.Model):
    question = models.TextField()
    correct_answer = models.TextField()
    answer_choice_a = models.TextField()
    answer_choice_b = models.TextField()
    answer_choice_c = models.TextField()
    answer_choice_d = models.TextField()
    chosen_answer = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
