from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'key': 'i am from html page'})


def result(request):
    article = request.GET['article']
    words = article.split()
    word_count = len(words)
    return render(request, 'result.html', {'article': article, 'word_count': word_count})
