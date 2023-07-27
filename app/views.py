from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage
# Create your views here.


# def mi_vista(request):
#     with open('database.json', encoding='utf-8') as file:
#         data = json.load(file)
#     return render(request, 'tabla.html',{'personas': data})

def mi_vista(request):
    with open('database.json', encoding='utf-8') as file:
        data = json.load(file)
    current_page = request.GET.get('pagina')
    
    if current_page:
        try:
            current_page = int(current_page)
            # items_per_page = 10  # Define la cantidad de elementos por página
            # start_idx = (current_page - 1) * items_per_page
            # end_idx = start_idx + items_per_page
            # data = data[start_idx:end_idx]
        except ValueError:
            pass

    return render(request, 'tabla.html', {'personas': data})

# def mi_vista(request):
#     with open('database.json', encoding='utf-8') as file:
#         data = json.load(file)

#     paginador = Paginator(data, 10)  # 10 registros por página

#     numero_pagina = request.GET.get('pagina')
#     if numero_pagina is None:
#         numero_pagina = 1

#     try:
#         pagina_actual = paginador.get_page(numero_pagina)
#     except EmptyPage:
#         pagina_actual = paginador.get_page(paginador.num_pages)

#     return render(request, 'tabla.html', {'pagina_actual': pagina_actual})