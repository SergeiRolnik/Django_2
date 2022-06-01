from django.http import HttpResponse
from django.shortcuts import render

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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def get_recipe(request, recipe):
    try:
        servings = int(request.GET.get('servings', 1))
    except:
        return HttpResponse("Введите целое число порций")
    recipe_data = DATA[recipe].copy()  # словарь с ингредиентами для конкретного рецепта (recipe)
    if servings != 1:
        for key, value in recipe_data.items():
            recipe_data[key] = value * servings
    context = {'recipe': recipe_data}
    return render(request, 'calculator/index.html', context)