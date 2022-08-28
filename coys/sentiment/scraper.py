import praw
from .models import User, Post, Comment

reddit = praw.Reddit(client_id='uce2S9EfyAp-BNw1L-z96g', client_secret='9uYyXFK4lFxOY5QB9dyXEEsuuhIlFA', user_agent='COYS Sentiment')

def loadPost():
    posts = reddit.subreddit("coys").new(limit=2)
    for post in posts:
        u = User(id=post.author.id, username = post.author.name)
        p = Post(id = post.id, title=post.title, body=post.selftext,user=u)
        u.save()
        p.save()

