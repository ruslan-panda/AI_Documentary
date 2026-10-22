from django.shortcuts import render

def home_page(request):
    # Эта функция отвечает за главную страницу.
    # Она говорит Django: «Возьми HTML-файл с именем index.html и покажи его».
    return render(request, 'index.html')
