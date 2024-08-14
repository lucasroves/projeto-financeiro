from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def resumo(request):
    return render(request, 'resumo.html')

def despesas(request):
    return render(request, 'despesas.html')

def vendas(request):
    return render(request, 'vendas.html')

def despesasXreceitas(request):
    return render(request,'despesasXreceitas.html')