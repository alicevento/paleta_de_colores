from flask import Flask, request, render_template, jsonify
import colorgram
from PIL import Image
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Validar si el archivo fue enviado en la solicitud
    if 'image' not in request.files:
        return jsonify({"error": "La imagen no ha sido cargada"}), 400

    # Obtener el archivo de la solicitud
    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No image selected"}), 400

    # Guardar la imagen temporalmente
    try:
        img = Image.open(image)
        img = img.convert("RGB")  # Asegurarse de que la imagen esté en RGB
        img.save('uploaded_image.jpg', format='JPEG')

        # Verificar si la imagen fue guardada
        if not os.path.exists('uploaded_image.jpg'):
            return jsonify({"error": "Error al guardar la imagen"}), 500
    except Exception as e:
        return jsonify({"error": f"Error al procesar la imagen: {str(e)}"}), 400

    # Extraer colores usando colorgram
    try:
        colores = colorgram.extract('uploaded_image.jpg', 10)  # Extraer los 10 colores más representativos
        colores_rgb = [{"r": color.rgb.r, "g": color.rgb.g, "b": color.rgb.b} for color in colores]
    except Exception as e:
        return jsonify({"error": f"Error al extraer colores: {str(e)}"}), 500

    # Limpiar la imagen temporal
    if os.path.exists('uploaded_image.jpg'):
        os.remove('uploaded_image.jpg')

    # Devolver los colores extraídos
    return jsonify(colores_rgb)

if __name__ == "__main__":
    app.run(debug=True)
