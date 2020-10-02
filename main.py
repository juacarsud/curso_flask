from flask import Flask, jsonify, request
import json

app = Flask(__name__)

libro = [
  {
    "indice": 1,
    "Titulo": "Yawar Fiesta",
    "Autor": "Jose_Maria_Arguedas"
  },
  {
    "indice": 2,
    "Titulo": "El Gallo Carmelo",
    "Autor": "Abraham Valdelomar"
  }
]

# Lectura de libros
@app.route('/libro', methods=["GET"])
def getAll():
  return jsonify(libro), 200

@app.route('/libro/<int:titulo>', methods=['GET'])
def obtenerlibro_titulo(titulo):
  result = next((l for l in libro if l["Titulo"] == titulo), None)
  if result is not None:
    return jsonify(result), 200
  else:
    return "<h1>404</h1><p>Libro no encontrado.</p>", 404

# Crear libro
@app.route('/libro', methods=["POST"])
def agregarlibro():
  body = json.loads(request.data)
  
  nuevoindice = body["indice"]
  nuevotitulo = body["Titulo"]
  nuevoautor = body["Autor"]

  nuevolibro = {
    "indice": nuevoindice,
    "Titulo": nuevotitulo,
    "autor": nuevoautor
  }

  libro.append(nuevolibro)
  return jsonify(nuevolibro), 200

# Borrar libro
@app.route('/libro/<int:indice>', methods=["DELETE"])
def eliminarlibro(indice):
  encontrarlibro = None
  for index, l in enumerate(libro):
    if l["indice"] == indice:
      encontrarlibro = l
      libro.pop(index)
  if encontrarlibro is not None:
    return "<h1>200</h1><p>Libro Eliminado.</p>", 200
  else:
    return "<h1>404</h1><p>Libro no encontrado.</p>", 404

# Actualizar libro
@app.route('/libro/<int:indice>', methods=["PUT"])
def actualizarlibro(indice):
  body = json.loads(request.data)

  nuevoindice = body["indice"]
  nuevotitulo = body["Titulo"]
  nuevoautor = body["Autor"]

  actualizarlibro = {
    "indice": nuevoindice,
    "Titulo": nuevotitulo,
    "Autor": nuevoautor
  }

  actlibro = None

  for index, l in enumerate(libro):
    if l["indice"] == indice:
      actlibro = actualizarlibro
      libro[index] = actualizarlibro
  
  if actlibro is not None:
    return "<h1>200</h1><p>Libro actualizado.</p>", 200
  else:
    return "<h1>404</h1><p>Libro no encontrado.</p>", 404

if __name__ == "__main__":
  app.run(debug=True, port=5001)