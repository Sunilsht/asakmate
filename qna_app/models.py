from django.db import models
class QuestionModel(models.Model):
    title=models.CharField(max_length=255)
    posted_by=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    question_desp=models.TextField()
    question_img=models.ImageField(upload_to="QuestionImg")


class AnswerModel(models.Model):
    ans_by=models.CharField(max_length=120)
    timestamp=models.DateTimeField(auto_now_add=True)
    answer_desp=models.TextField()
    answers_img=models.ImageField(upload_to="AnswersImg")
    is_accepted=models.BooleanField()
    votes =models.models.IntegerField()
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    




# Create your models here.
