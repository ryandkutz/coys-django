import praw
from .models import User, Post, Comment

reddit = praw.Reddit(client_id='uce2S9EfyAp-BNw1L-z96g', client_secret='9uYyXFK4lFxOY5QB9dyXEEsuuhIlFA', user_agent='COYS Sentiment')

#need sentiment scoring for all of this

def loadPostsNew(lim):
    posts = reddit.subreddit("coys").new(limit=lim)
    for post in posts:
        u = User(id=post.author.id, username = post.author.name)
        p = Post(id=post.id, title=post.title, body=post.selftext,user=u)
        u.save()
        p.save()
def loadPostByID(postID):
    print("loading post")
    post = reddit.submission(id=postID)
    u = User(id=post.author.id, username = post.author.name)
    p = Post(id=post.id, title=post.title, body=post.selftext,user=u)
    u.save()
    p.save()
    print("loaded post")
def loadComments(postID):
    post = reddit.submission(id=postID)
    p = Post.objects.get(pk=postID)
    post.comments.replace_more(limit=None)
    for comment in post.comments.list():
        try:
            u = User.objects.get(pk=comment.author.id)
        except User.DoesNotExist:
            u = None
        if u:
            c = Comment(id=comment.id,post=p,body=comment.body,user=u)
            c.save()
            print("loaded existing user's comment")
            pass
        else:
            u = User(id=comment.author.id, username=comment.author.name)
            u.save()
            c = Comment(id=comment.id,post=p,body=comment.body,user=u)
            c.save()
            print("loaded new user's comment")
            pass

