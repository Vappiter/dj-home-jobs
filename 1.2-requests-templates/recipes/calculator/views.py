import copy

from django.shortcuts import render, reverse

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Вариант №1 с использованием модуля COPY': reverse('recipes_1'),
        'Вариант №2 с использованием передачи DATA в качестве аргумента': reverse('recipes_2'),
        
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def recipes_view_1(request, var1 = ''):
  global DATA  
  data1 = {}
  data1 = copy.deepcopy (DATA)
  serving = int(request.GET.get("serving", 1))  
  if var1 ==  '':
   context = {}
  else:
   for x in data1:
     if var1 == x:
      for y in data1[var1]:  
        data1[var1][y] = data1[var1][y] * serving 
      context = {
        'recipe':data1[var1],
        'serving':serving
        }
      break
     else: 
      context = {}
      
  return render(request, 'calculator/index.html',context)

# Не рабочий вариант :(

def recipes_view_2(request, var1 = '', data1 = DATA):
  serving = int(request.GET.get("serving", 1))  
  if var1 ==  '':
   context = {}
  else:
   for x in data1:
     if var1 == x:
      for y in data1[var1]:  
        data1[var1][y] = data1[var1][y] * serving 
      context = {
        'recipe':data1[var1],
        'serving':serving
        }
      break
     else: 
      context = {}
  data1 = {}    
  return render(request, 'calculator/index.html',context)