from json import loads
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests import get
import requests


@login_required
def airports_view(request):
    location = request.GET.get('location')
    context = {}
    if location:
        city_location = location.title()
        if airports_json_city(city_location) != -1:
            icao_code = airports_json_city(city_location)['icao']
            data = get_airport(icao_code)
            context = {'data': data}
        elif get_airport(location) != -1:
            data = get_airport(location)
            context = {'data': data}
        else:
            error = "Airport not found, enter correct ICAO code. You can find it "
            context = {'error': error}

    return render(request, "aviation_app/airports.html", context)


@login_required
def metar_view(request):
    location = request.GET.get('location')
    context = {}
    if location:
        city_location = location.title()
        if airports_json_city(city_location) != -1:
            icao_code = airports_json_city(city_location)['icao']
            data = get_metar(icao_code)
            context = {'data': data}
        elif get_airport(location) != -1:
            data = get_metar(location)
            context = {'data': data}
        else:
            error = "METAR not found, enter correct ICAO code. You can find it "
            context = {'error': error}

    return render(request, "aviation_app/metar.html", context)


@login_required
def taf_view(request):
    location = request.GET.get('location')
    context = {}
    if location:
        city_location = location.title()
        if airports_json_city(city_location) != -1:
            icao_code = airports_json_city(city_location)['icao']
            data = get_taf(icao_code)
            context = {'data': data}
        elif get_airport(location) != -1:
            data = get_taf(location)
            context = {'data': data}
        else:
            error = "TAF not found, enter correct ICAO code. You can find it "
            context = {'error': error}

    return render(request, "aviation_app/taf.html", context)

@login_required
def significant_view(request):
    return render(request, "aviation_app/significant.html")


def get_metar(icao_code):
    hdr = {"X-API-Key": "0dd3ac44540e49fa8d844d3110"}
    req = get(f'https://api.checkwx.com/metar/{icao_code}', headers=hdr)

    try:
        req.raise_for_status()
        resp = loads(req.text)
        if resp['data']:
            return (resp['data'])[0]

    except requests.exceptions.HTTPError as e:
        print(e)


def get_airport(icao_code):
    hdr = {"X-API-Key": "0dd3ac44540e49fa8d844d3110"}
    req = get(f'https://api.checkwx.com/station/{icao_code}', headers=hdr)

    try:
        req.raise_for_status()
        resp = loads(req.text)
        if resp['data']:
            formatted_data = airport_data_formatter((resp['data'])[0])
            return formatted_data
        else:
            return -1

    except requests.exceptions.HTTPError as e:
        print(e)


def airport_data_formatter(data):
    print(data)
    data_list = []
    text = ""
    for key, value in data.items():
        if str(value).startswith('{'):
            text = f"<b>{key.upper()}:</b> "
            for key2, value2 in value.items():
                text = text  + f" {key2}: {value2}" + ", "
            data_list.append(text)
            text = ""
        else:
            data = f"<b>{key.upper()}:</b> {value}"
            data_list.append(data)

    return data_list


def airports_json_city(city):
    with open('aviation_app/airports.json') as f:
        data = json.load(f)

    for i in data:
        if i["city"] == city:
            return i
    else:
        return -1


def get_taf(icao_code):
    hdr = {"X-API-Key": "0dd3ac44540e49fa8d844d3110"}
    req = get(f'https://api.checkwx.com/taf/{icao_code}', headers=hdr)

    try:
        req.raise_for_status()
        resp = loads(req.text)
        if resp['data']:
            return (resp['data'])[0]
        else:
            return -1

    except requests.exceptions.HTTPError as e:
        print(e)

