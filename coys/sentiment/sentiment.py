from transformers import pipeline
from .models import User, Post, Comment

sentiment_pipeline = pipeline("sentiment-analysis")

def getCommentScore(text):
    return sentiment_pipeline(text)