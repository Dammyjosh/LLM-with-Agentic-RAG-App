from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=150):
    text = text[:1500]
    return summarizer(text, max_length=max_length, min_length=40, do_sample=False)[0]["summary_text"]