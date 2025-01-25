from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=268)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.title} - {self.updated_date}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.created_date}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='votes')

    def __str__(self):
        return f"{self.user} liked {self.question.title}"
