from django.shortcuts import render, HttpResponse
import requests

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value}
            response = requests.post('http://127.0.0.1:8081/measures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8081/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})

def cultivo(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'codigo' in request.GET and 'latitud' in request.GET and 'longitud' in request.GET and 'area' in request.GET and 'producto' in request.GET:
        codigo   = request.GET['codigo']
        latitud  = request.GET['latitud']
        longitud = request.GET['longitud']
        area     = request.GET['area']
        producto = request.GET['producto']

        # Verifica si el value no esta vacio
        if codigo and latitud and longitud and area and producto:
            if int(area) >= 0:
                # Crea el json para realizar la petición POST al Web Service
                args = {'codigo': int(codigo), 'latitud': int(latitud), 'longitud': int(longitud), 'area':int(area), 'producto':producto}
                print(args)
                response = requests.post('http://127.0.0.1:8081/cultivo/', args)
                # Convierte la respuesta en JSON
                measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8081/cultivo/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/cultivo.html", {'measures': measures})
    #return render(request, "measure/measure.html", {'measures': measures})