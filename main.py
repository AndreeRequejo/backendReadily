from flask import Flask
from flask_jwt_extended import jwt_required, JWTManager
# Import Controladores
import controller.auth_controller as auth_controller
import controller.usuario_controller as usuario_controller

app = Flask(__name__)
app.debug = True
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

# Ruta de autenticación
@app.route("/auth", methods=["POST"])
def auth():
    return auth_controller.auth()

# Ruta protegida y retorno de usuario
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return auth_controller.protected()

# Ruta para registrar un nuevo usuario
@app.route("/api_registrarusuario", methods=["POST"])
def register():
    return usuario_controller.registrarUsuario()

@app.route("/")
def home():
    valor = "Grupo 01"
    return f"<p>Bienvenido, {valor}</p>"

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)