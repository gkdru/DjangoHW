from statistics import mode
from django.db import models
from django.urls import reverse


class Question(models.Model):
    # QTYPE = {"O": "Open", "C": "Closed", "I": "Ilyas"}
    # qtype = models.CharField(max_length=100, choices=QTYPE)
    question_text = models.CharField(max_length=200)
    comment = models.CharField(max_length=300, null=True, blank=True)
    pub_date = models.DateTimeField("date published",null=True, blank=True)

    def __str__(self) -> str:
        return self.question_text
    class Meta:
        get_latest_by = 'pub_date'

    def get_absolute_url(self):
        return reverse('polls:detail', kwargs={"question_id": self.id})


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
