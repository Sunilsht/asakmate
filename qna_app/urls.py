from django.urls import path
from .views import addquestions
urlpatterns = [
    path('addquestions/', addquestions, name='addquestions')
]
