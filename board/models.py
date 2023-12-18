from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    teacher = models.ForeignKey(User, related_name='board_topics', on_delete=models.CASCADE, null=True) 
    date = models.DateField(auto_now_add=True, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField(null=True)

class Reply(models.Model):
    message = models.TextField(max_length=5000)
    updated_at = models.DateField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='replies', on_delete=models.CASCADE)

class BoardQa(models.Model):
    learner = models.ForeignKey(User, related_name='qa_topics', on_delete=models.CASCADE, null=True) 
    date = models.DateField(auto_now_add=True, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField(null=True)

class Reply2(models.Model):
    message = models.TextField(max_length=5000)
    updated_at = models.DateField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='qa_replies', on_delete=models.CASCADE)

class BoardShare(models.Model):
    learner = models.ForeignKey(User, related_name='share_topics', on_delete=models.CASCADE, null=True) 
    date = models.DateField(auto_now_add=True, null=True)
    subject = models.CharField(max_length=200)
    content = models.TextField(null=True)

class Reply3(models.Model):
    message = models.TextField(max_length=5000)
    updated_at = models.DateField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='share_replies', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.message


