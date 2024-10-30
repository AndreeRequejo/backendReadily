from flask import Flask, jsonify
from flask_jwt_extended import jwt_required, JWTManager
# Import Controladores
import controller.auth_controller as auth_controller
from models.Usuario import Usuario

app = Flask(__name__)
app.debug = True
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

@app.route("/auth", methods=["POST"])
def auth():
    return auth_controller.auth()

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return auth_controller.protected()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)