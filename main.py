from flask import Flask, request, jsonify
from flask_jwt_extended import jwt_required, JWTManager, create_access_token
# Import Controladores
import db.database as db
import controller.auth_controller as auth_controller
import controller.usuario_controller as usuario_controller
import controller.libro_controller as libro_controller
import stripe

app = Flask(__name__)
app.debug = True
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

# Ruta de autenticación
@app.route("/auth", methods=["POST"])  # Cambié el nombre de esta ruta y función
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

# Ruta para obtener el libro completo
@app.route("/api_libro", methods=["GET"])
def libro_completo():
    return libro_controller.libro_completo()

# Ruta para obtener un libro específico por isbn_lib
@app.route("/api_libro/<string:isbn_lib>", methods=["GET"])
def libro_por_isbn(isbn_lib):
    return libro_controller.libro_por_isbn(isbn_lib)

# Ruta para obtener libros comprados por un usuario específico
@app.route("/api_libros_comprados/<string:email_user>", methods=["GET"])
def libros_comprados_por_usuario(email_user):
    return libro_controller.libros_comprados_por_usuario(email_user)


# Nueva ruta para libros más vendidos
@app.route("/api_libros_mas_vendidos", methods=["GET"])
def libros_mas_vendidos():
    return libro_controller.libros_mas_vendidos()

# Ruta para obtener libros antiguos
@app.route("/api_libros_antiguos", methods=["GET"])
def libros_antiguos():
    return libro_controller.libros_antiguos()

# Ruta para obtener libros actuales
@app.route("/api_libros_actuales", methods=["GET"])
def libros_actuales():
    return libro_controller.libros_actuales()

# Nueva ruta para los mejores autores y sus libros
@app.route("/api_mejores_autores_libros", methods=["GET"])
def mejores_autores_libros():
    return libro_controller.mejores_autores_libros()

# Ruta para retornar el preview del libro
@app.route("/api_libro/<string:libro_id>", methods=["GET"])
def obtener_libro(libro_id):
    return libro_controller.obtener_preview_libro_por_id(libro_id)

from flask import Flask
# Importa el controlador de ventas
import controller.venta_controller as venta_controller

# Nueva ruta para guardar la venta
@app.route("/api_guardar_venta", methods=["POST"])
def guardar_venta():
    return venta_controller.guardar_venta()

@app.route('/api_obtener_dni_lec', methods=['POST'])
def obtener_dni_lec():
    try:
        data = request.json
        email_user = data.get("email_user")

        if not email_user:
            return jsonify({"code": 1, "msg": "Correo electrónico no proporcionado"}), 400

        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT l.dni_lec FROM lector l
                    JOIN usuario u ON l.id_user = u.id_user
                    WHERE u.email_user = %s
                """, (email_user,))
                result = cursor.fetchone()

        if result:
            return jsonify({"code": 0, "dni_lec": result[0]}), 200
        else:
            return jsonify({"code": 1, "msg": "No se encontró el dni_lec para el correo proporcionado"}), 404
    except Exception as e:
        return jsonify({"code": 1, "msg": f"Error al obtener el dni_lec: {str(e)}"}), 500


stripe.api_key = ''

@app.route('/payment-sheet/<int:total>', methods=['POST'])
def payment_sheet(total):
  # Use an existing Customer ID if this is a returning customer
  customer = stripe.Customer.create()
  ephemeralKey = stripe.EphemeralKey.create(
    customer=customer['id'],
    stripe_version='2024-10-28.acacia',
  )

  paymentIntent = stripe.PaymentIntent.create(
    amount=total,
    currency='eur',
    customer=customer['id'],
    # In the latest version of the API, specifying the `automatic_payment_methods` parameter
    # is optional because Stripe enables its functionality by default.
    automatic_payment_methods={
      'enabled': True,
    },
  )
  return jsonify(paymentIntent=paymentIntent.client_secret,
                 ephemeralKey=ephemeralKey.secret,
                 customer=customer.id,
                 publishableKey='')

#! Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
