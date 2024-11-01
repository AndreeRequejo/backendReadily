import bcrypt
from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity
# Importación de servicios
import services.usuario_service as usuario_service
# Importación de modelos
from models.Usuario import Usuario

def auth():
    # Body del Request
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # Validar credenciales del usuario
    try:
        usuario = usuario_service.obtener_usuario(email)
        if usuario:
            email_almacenado = usuario[1]
            hash_almacenado = usuario[2]

            # Verificar la contraseña usando bcrypt
            if email == email_almacenado and bcrypt.checkpw(password.encode('utf-8'), hash_almacenado.encode('utf-8')):
                user = Usuario(usuario[0], email, password)
                access_token = create_access_token(identity=user.email_user)
                return jsonify(access_token=access_token), 200
            else:
                return jsonify({"msg": "Credenciales incorrectas"}), 401
        else:
            return jsonify({"msg": "Usuario no encontrado"}), 404
    except Exception as e:
        print("Error en autenticación:", e)
        return jsonify({"msg": "Error durante autenticación"}), 500

def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
