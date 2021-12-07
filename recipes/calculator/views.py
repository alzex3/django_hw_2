from django.shortcuts import render
from django.conf import settings


def calc(request, dish):
    recipe = settings.DATA.get(dish)

    if recipe:
        recipe = recipe.copy()
        servings = int(request.GET.get('servings', 1))

        for key, value in recipe.items():
            recipe[key] = value * servings

    context = {
        'recipe': recipe
    }

    return render(request, 'calculator/index.html', context)
