from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Хороший магазин, только заказть Вы ничего не сможете, т.к. у писателя сайта руки из одного места расут",
    }
    return render(request, "main/about.html", context)


def dostavka(request):
    context = {
        "title": "Доставка",
        "content": "Доставка и оплата",
        "text_on_page": "Время доставки 9.00 - 20.00",
    }
    return render(request, "main/dostavka.html", context)


def contacts(request):
    context = {
        "title": "Контакты",
        "content": "Наши контакты",
        "text_on_page": "8 029 555 66 77 Елена",
    }
    return render(request, "main/contacts.html", context)
