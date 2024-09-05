# LFN_vehicle_proy
Proyecto de LFN Vehicle
Proyecto realizado con el framework flask de python
Pasos para utilizar flask en python
Paso 1: Instalación de Flask

    Instala Flask utilizando pip si aún no lo tienes:

    bash

    pip install Flask

Paso 2: Configuración del Proyecto

    Crea una carpeta para tu proyecto Flask y navega hasta ella:

    bash

mkdir flask-github-manual
cd flask-github-manual

Crea un entorno virtual para manejar las dependencias:

bash

    python -m venv venv
    source venv/bin/activate  # Para Linux/Mac
    venv\Scripts\activate  # Para Windows

Paso 3: Crear el Archivo Principal de la Aplicación

    Crea un archivo app.py y añade el siguiente código básico de Flask:

    python

    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('index.html')

    if __name__ == '__main__':
        app.run(debug=True)

Paso 4: Crear las Plantillas HTML

    Crea una carpeta templates en la raíz de tu proyecto.

    Dentro de templates, crea un archivo index.html con contenido HTML básico. Este archivo puede contener tu manual de GitHub:

    html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Manual de GitHub</title>
    </head>
    <body>
        <h1>Bienvenido al Manual de GitHub</h1>
        <p>En este manual aprenderás cómo usar GitHub para el control de versiones y la colaboración en proyectos.</p>
        <!-- Agrega aquí más contenido como secciones de tu manual -->
    </body>
    </html>

Paso 5: Ejecutar la Aplicación

    Ejecuta la aplicación Flask usando el siguiente comando:

    bash

    python app.py

    Visita http://127.0.0.1:5000/ en tu navegador para ver tu página web.

Paso 6: Agregar Contenido Dinámico

    Edita el archivo index.html y cualquier otro archivo de plantilla para agregar más secciones o contenido detallado del manual de GitHub, como comandos, ejemplos de código, o tutoriales.

Paso 7: Implementar Estilos y Funcionalidades

    Agrega CSS para estilizar la página y mejorar la presentación. Puedes crear un archivo CSS en una carpeta llamada static:

    bash

mkdir static

En static, crea un archivo style.css y enlázalo en tus plantillas HTML:

html

    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

