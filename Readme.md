# Mapa de "profes" de Python de Argentina

## ¿Cómo me sumo al mapa?

* **Fork**  de este repo.

![](https://help.github.com/assets/images/help/repository/fork_button.jpg)

* Clonar el repo.

`git clone https://github.com/<usuario>/mapa-pyar-docentes`

* Instalar librerías.

`pip install -r requirements.txt`

* Editar el archivo `map/data.yaml`, *agregandp al final* las siguientes líneas (procurando dejar un salto de línea):

```yaml
- nombre: ''
  ubicacion:
    latitud: 
    longitud:
  lugar:
    #'academia'
    #'particular'
    #'escuela/universidad'
    #'remoto'
    #'otro'
  nivel:
    #'basico'
    #'intermedio'
    #'avanzado'
  contacto: ''
```

*NOTA:* Se deben editar los campos `nombre` (debe ser un string), `latitud`, `longitud` (float, sin comillas), `contacto`, *descomentar* la opción correspondiente (sólo una) para lugar y nivel.

* **Ejecutar el script** `map/mapa-pyar-docentes.py`

`python mapa-pyar-docentes.py`

* Agregar los cambios:

`git add map/data.yaml map/mapa-pyar-docentes.py`

`git commit -m 'punto del profe <nombre del profe> agregado'

`git push`

* Hacer un **pull request**

![](https://help.github.com/assets/images/help/pull_requests/pull-request-start-review-button.png)

[Más info sobre pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
