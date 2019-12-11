from django.db import models


class QuestionModel(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    que_votes = models.IntegerField(default=0)
    question_desp = models.TextField()
    question_img = models.ImageField(
        upload_to="QuestionImg", blank=True, null=True)

    def __str__(self):
        return self.question_desp


class AnswerModel(models.Model):
    ans_by = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    answer_desp = models.TextField()
    answers_img = models.ImageField(
        upload_to="AnswersImg", blank=True, null=True)
    is_accepted = models.BooleanField(default=0)
    ans_votes = models.IntegerField(default=0)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    #objects =object.models.Manager() for grey box

    def __str__(self):
        return self.answer_desp


# Create your models here.
