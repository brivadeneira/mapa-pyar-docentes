#!/usr/bin/env python
# coding: utf-8

# In[116]:


import folium
import yaml


# In[117]:


with open(r'data.yaml') as file:
    data_map = yaml.full_load(file)


# In[121]:


def map_icon(key):
    map_icon_dict = {
    'academia': 'book',
    'particular': 'home',
    'escuela/universidad': 'university',
    'remoto': 'laptop',
    'otro': 'handshake-o'
        }
    return map_icon_dict[key]

def color_icon(key):
    icon_color_dict = {
        'basico': 'lightblue',
        'intermedio': 'blue',
        'avanzado': 'cadetblue'
    }
    return icon_color_dict[key]


# In[122]:


py_map = folium.Map(location=[-34.6131500, -58.3772300], 
                    zoom_start=3.5)
for docente in data_map['docentes']:
    lat = docente['ubicacion']['latitud']
    lon = docente['ubicacion']['longitud']
    etiqueta = docente['nombre'] + ', ' + docente['lugar'] + ': ' + docente['contacto']
    icon = map_icon(docente['lugar'])
    color = color_icon(docente['nivel'])
    folium.Marker(location=[lat,lon], 
                  popup=etiqueta, 
                      icon=folium.Icon(color=color,icon=icon, prefix='fa')).add_to(py_map)
py_map.save("./map-pyar-docentes.html")

