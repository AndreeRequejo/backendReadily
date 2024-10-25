from flask import Flask, render_template, request, redirect, flash, jsonify
import hashlib
import controller.auth_controller as auth_controller
import services.lector_service as lector_service
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, auth_controller.authenticate, auth_controller.identity)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/lector/<email>", methods=["GET"])
@jwt_required()
def obtener_datos_lector(email):
    lector = lector_service.obtener_lector(email)
    if lector:
        lector_data = {
            "dni": lector[0],
            "nombre": lector[1],
            "apellido_paterno": lector[2],
            "apellido_materno": lector[3],
            "email": lector[4],
            "fecha_nacimiento": lector[6]
        }
        return jsonify(lector_data), 200  # Respuesta exitosa
    else:
        return jsonify({"message": "Lector no encontrado"}), 404  # No encontrado

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)