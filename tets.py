# data = {
#     'omlet': {'яйца, шт': 2, 'молоко, л': 0.1, 'соль, ч.л.': 0.5},
#      'pasta': {'макароны, г': 0.3, 'сыр, г': 0.05},
#      'buter': {'хлеб, ломтик': 1, 'колбаса, ломтик': 1, 'сыр, ломтик': 1, 'помидор, ломтик': 1},
#     'servings': 3}


p = 2
context = {}
data = {'яйца, шт': 6,
        'молоко, л': 0.30000000000000004,
        'соль, ч.л.': 1.5}

context ['omlet'] = data
print(context)