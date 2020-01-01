#!/usr/bin/env python
# coding: utf-8
import folium
import yaml


with open(r"data.yaml") as file:
    data_map = yaml.full_load(file)


def map_icon(key):
    map_icon_dict = {
        "academia": "book",
        "particular": "home",
        "escuela/universidad": "university",
        "remoto": "laptop",
        "otro": "handshake-o",
    }
    return map_icon_dict[key]


def color_icon(key):
    icon_color_dict = {
        "basico": "lightblue",
        "intermedio": "blue",
        "avanzado": "cadetblue",
    }
    return icon_color_dict[key]


py_map = folium.Map(
    location=[-40.38, -67.15],
    max_bounds=True,
    min_zoom=3,
    max_zoom=18,
    zoom_start=3.5,
    min_lat=-56.3,
    max_lat=-21.4,
    min_lon=-77.4,
    max_lon=-52.7,
)
for docente in data_map["docentes"]:
    lat = docente["ubicacion"]["latitud"]
    lon = docente["ubicacion"]["longitud"]
    etiqueta = docente["nombre"] + ", " + docente["lugar"] + ": " + docente["contacto"]
    icon = map_icon(docente["lugar"])
    color = color_icon(docente["nivel"])
    folium.Marker(
        location=[lat, lon],
        popup=etiqueta,
        icon=folium.Icon(color=color, icon=icon, prefix="fa"),
    ).add_to(py_map)
py_map.save("./map-pyar-docentes.html")
