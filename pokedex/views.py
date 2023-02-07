# Python
import urllib.request
import json

# Django
from django.shortcuts import render
from django.http import HttpResponse
from http import HTTPStatus
from urllib.error import HTTPError

def index(request):
    try:
        if request.method == 'POST':        # pregunto si la solitud recibida es POST
            pokemon = request.POST['pokemon'].lower()        # almaceno el dato enviado por el usuario, en este caso el nombre del pokemon
            pokemon = pokemon.replace(' ', '')        # elimino espacios en la cadena
            url_pokeapi = urllib.request.Request(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')        # definimos la url
            url_pokeapi.add_header('User-Agent', 'Charmander')        # mostrar un encabezado
            source = urllib.request.urlopen(url_pokeapi).read()        # hacemos un get y leemos el contenido de la respuesta, obtenemos el json
            data_api = json.loads(source)        # convertimos el json a lista/diccionario
            
            # altura de decimetros a metros
            height_m = (float((data_api['height'])*0.1))
            height_m = round (height_m, 2)

            # peso de hectogramos a kilogramos
            weight_kg = (float((data_api['weight'])*0.1))
            weight_kg = round(weight_kg, 2)
            
            data = {
                'name': str(data_api['name']).capitalize(),
                'number': str(data_api['id']),
                'height': str(height_m) + ' m',
                'weight': str(weight_kg) + ' kg',
                'sprite': str(data_api['sprites']['front_default']),     
            }
            print(data)
        else: 
            data = {}
    
        return render(request, 'pokedex/index.html', data)
    except HTTPError as e:        # el error que esperamos
        if e.code == 404:
            return render(request, 'pokedex/404.html')
