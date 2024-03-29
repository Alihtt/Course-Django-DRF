from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='questions')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.username} - {self.title[:20]}'


class Answer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self) -> str:
        return f'{self.user.username} - {self.title[:20]}'
