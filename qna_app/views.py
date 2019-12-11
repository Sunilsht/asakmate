from django.shortcuts import render
from .models import QuestionModel


def addquestions(request):
    question = QuestionModel.objects.all()
    return render(request,'newquestion.htm', {'que': question})
# Create your views here.
