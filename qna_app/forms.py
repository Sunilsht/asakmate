from .models import QuestionModel,AnswerModel
from django import forms
class QuestionForm(forms.ModelForm):
    class Meta:
        model=QuestionForm
        fields='__all__'
         