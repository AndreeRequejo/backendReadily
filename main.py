from flask import Flask, jsonify
#import hashlib
from flask_jwt import JWT, jwt_required
import services.usuario_service as usuario_service

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

def authenticate(username, password):
    try:
        usuario = usuario_service.obtener_usuario(username)
        if usuario and usuario["pass_user"].encode('utf-8') == password.encode('utf-8'):
            return User(usuario["id_user"], username, usuario["pass_user"])
    except:
        return None
    
def identity(payload):
    try:
        user_id = payload['identity']
        usuario = usuario_service.obtener_credenciales(user_id)
        user = User(user_id, usuario["email_user"], usuario["pass_user"])
        return user
    except:
        return None

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/lector/<email>", methods=["GET"])
@jwt_required
def obtener_datos_user(email):
    usuario = usuario_service.obtener_usuario(email)
    if usuario:
        usuario_data = {
            "id": usuario["id_user"],
            "email": usuario["email_user"],
            "pass": usuario["pass_user"]
        }
        return jsonify(usuario_data), 200  # Respuesta exitosa
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404  # No encontrado
    
@app.route("/user/<id>", methods=["GET"])
def obtener_datos(id):
    usuario = usuario_service.obtener_credenciales(id)
    if usuario:
        usuario_data = {
            "id": usuario[0],
            "email": usuario[1],
            "pass": usuario[2]
        }
        return jsonify(usuario_data), 200  # Respuesta exitosa
    else:
        return jsonify({"message": "Usuario no encontrado"}), 404  # No encontrado

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)