from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, valor_a, valor_b):
    return HttpResponse("<h2>Soma: {} + {} = {}</h2>".format(valor_a, valor_b, (valor_a+valor_b)))

def subtracao(request, valor_a, valor_b):
    return HttpResponse("<h2>Subtração: {} - {} = {}</h2>".format(valor_a, valor_b, (valor_a-valor_b)))

def multiplicacao(request, valor_a, valor_b):
    return HttpResponse("<h2>Multiplicação: {} * {} = {}</h2>".format(valor_a, valor_b, (valor_a*valor_b)))

def divisao(request, valor_a, valor_b):
    return HttpResponse("<h2>Divisão: {} / {} = {}</h2>".format(valor_a, valor_b, (valor_a/valor_b)))