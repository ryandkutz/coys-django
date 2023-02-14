import praw
from .models import User, Post, Comment
from . import sentiment

reddit = praw.Reddit(client_id='CLIENT-ID', client_secret='CLIENT-SECRET', user_agent='COYS Sentiment')

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
            c = Comment(id=comment.id,post=p,body=comment.body,user=u,author=u.username)
            sentiment_data = sentiment.getCommentScore(c.body)
            c.sentimentClass = sentiment_data[0]["label"]
            c.sentimentScore = sentiment_data[0]["score"]
            c.save()
            print("loaded comment from existing user " + c.user.username)
            pass
        else:
            u = User(id=comment.author.id, username=comment.author.name)
            u.save()
            c = Comment(id=comment.id,post=p,body=comment.body,user=u,author=u.username)
            sentiment_data = sentiment.getCommentScore(c.body)
            c.sentimentClass = sentiment_data[0]["label"]
            c.sentimentScore = sentiment_data[0]["score"]
            c.save()
            print("loaded comment from new user " + c.user.username)
            pass
def loadUserComments(uname):
    target, created = User.objects.get_or_create(id=reddit.redditor(uname).id, username=uname)
    for comment in reddit.redditor(uname).comments.new(limit=10):
        if comment.subreddit.display_name == "coys":
            u, created = User.objects.get_or_create(id=comment.submission.author.id, username=comment.submission.author.name)
            p, created = Post.objects.get_or_create(id=comment.submission.id,title=comment.submission.title,body=comment.submission.selftext,user=u)
            c = Comment(id=comment.id,post=p,body=comment.body,user=target,author=target.username)
            sentiment_data = sentiment.getCommentScore(c.body)
            c.sentimentClass = sentiment_data[0]["label"]
            c.sentimentScore = sentiment_data[0]["score"]
            c.save()
            print(c.body)

