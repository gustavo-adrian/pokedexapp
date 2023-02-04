# Python
import urllib.request
import json

# Django
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':        # pregunto si la solitud recibida es POST
        pokemon = request.POST['pokemon'].lower()        # almaceno el dato enviado por el usuario, en este caso el nombre del pokemon
        pokemon = pokemon.replace(' ', '')        # elimino espacios en la cadena
        url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')        # definimos la url
        url_pokeapi.add_header('User-Agent', 'Charmander')        # mostrar un encabezado
        source = urllib.request.urlopen(url_pokeapi).read()        # hacemos un get y leemos el contenido de la respuesta, obtenemos el json
        data_api = json.loads(source)        # convertimos el json a lista/diccionario
        data = {
            'number': str(data_api['id']),
            'name': str(data_api['name']).capitalize(),
            'height': str(data_api['height']),
            'weight': str(data_api['weight']),
            'sprite': str(data_api['sprites']['front_default']),     
        }
        print(data)
    else: 
        data = {}

    return render(request, 'pokedex/index.html', data)

