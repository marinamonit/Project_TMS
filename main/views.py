from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о магазине",
    }
    return render(request, "main/about.html", context)


def dostavka(request):
    context = {
        "title": "Доставка",
        "content": "Доставка и оплата",
        "text_on_page": "Текст о доставке и оплате",
    }
    return render(request, "main/dostavka.html", context)


def contacts(request):
    context = {
        "title": "Контакты",
        "content": "Наши контакты",
        "text_on_page": "Данные контактов",
    }
    return render(request, "main/contacts.html", context)
