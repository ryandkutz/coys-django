from django.db import models

class User(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    username = models.CharField(max_length=100)
    sentimentClass = models.TextField(max_length=100, default="null")
    sentimentScore = models.DecimalField(max_digits=18,decimal_places=16, default = 0.0)
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
    author = models.CharField(max_length=100, default="null")
    sentimentClass = models.TextField(max_length=100, default="null")
    sentimentScore = models.DecimalField(max_digits=18,decimal_places=16, default=0.0)
    
