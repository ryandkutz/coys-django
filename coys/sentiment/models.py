from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=100)
    sentiment = models.TextField(max_length=100, default="null")
class Post(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.TextField(max_length=300)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Comment(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sentiment = models.TextField(max_length=100, default="null")
    
