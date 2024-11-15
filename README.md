```markdown
# Generador de Paleta de Colores

Este proyecto es una aplicación web que permite a los usuarios subir una imagen y generar una paleta de colores a partir de ella. Utiliza Flask como framework para el backend, junto con la librería `colorgram` para la extracción de colores y `Pillow` para el manejo de imágenes. El frontend está construido con HTML, CSS (Bootstrap) y JavaScript.

## :star: Características
- Subir una imagen colores predominantes.
- Mostrar la paleta de colores generada en formato RGB, HEX y CMYK.
- Interfaz de usuario simple y fácil de usar, desarrollada con Bootstrap.

## :package: Requisitos
- Python 3.x
- Flask
- Pillow
- colorgram.py

## :gear: Instalación
1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/generador-paleta-colores.git
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd generador-paleta-colores
   ```
3. Crea un entorno virtual e instálalo:
   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```
4. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```
   El archivo `requirements.txt` debe contener:
   ```
   Flask
   Pillow
   colorgram.py
   ```

## :rocket: Uso
1. Inicia la aplicación ejecutando el siguiente comando:
   ```sh
   python app.py
   ```
2. Abre tu navegador web y visita `http://127.0.0.1:5000`.
3. Sube una imagen y haz clic en "Generar Paleta".

## :file_folder: Archivos Principales
- `app.py`: Código del backend usando Flask.
- `templates/index.html`: Página principal de la aplicación con el formulario para subir imágenes.
- `static/`: Contiene los archivos CSS y JavaScript.

## :hammer: Funcionalidad
- El usuario sube una imagen y hace click en "Generar paleta".
- El servidor procesa la imagen, extrae los colores predominantes y devuelve la paleta de colores.
- La interfaz muestra la imagen cargada y la paleta de colores, incluyendo valores en RGB, HEX y CMYK.

## :computer: Tecnologías Utilizadas
- **Flask**: Framework para el desarrollo del backend.
- **Pillow**: Librería para el manejo de imágenes.
- **colorgram**: Herramienta para la extracción de colores de una imagen.
- **Bootstrap**: Framework CSS para crear una interfaz moderna y responsiva.

## :bulb: Mejoras Futuras
- Añadir la funcionalidad para guardar la paleta de colores generada en un archivo.
- Permitir la extracción de más colores, dependiendo del rendimiento.
- Implementar autenticación para que los usuarios puedan guardar y gestionar sus paletas de colores.

## :busts_in_silhouette: Autor
- Desarrollado por Alicia Vento.






# paleta_de_colores
