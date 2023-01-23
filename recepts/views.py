from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def hello_view(request):
    return HttpResponse ('Выберете блюдо:')

def omlet_view(request): #omlet/?2
    servings = int(request.GET.get('servings', 1))
    omlet = {}
    context = {}
    for k, v in DATA['omlet'].items():
        v = v * servings
        omlet[k] = round(v, 2)

    context ['omlet'] = omlet
    return render(request, 'omlet.html', context)


def pasta_view(request):
    servings = int(request.GET.get('servings', 1))
    pasta = {}
    context = {}
    for k, v in DATA['pasta'].items():
        v = v * servings
        pasta[k] = round(v, 2)

    context ['pasta'] = pasta
    return render(request, 'pasta.html', context)

def buter_view(request):
    servings = int(request.GET.get('servings', 1))
    buter = {}
    context = {}
    for k, v in DATA['buter'].items():
        v = v * servings
        buter[k] = round(v, 2)

    context ['buter'] = buter
    return render(request, 'buter.html', context)
    


