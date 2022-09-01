from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def getCommentScore(text):
    return sentiment_pipeline(text)