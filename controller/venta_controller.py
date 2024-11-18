from flask import request, jsonify
import db.database as db

def guardar_venta():
    try:
        data = request.json
        id_user = data.get("id_user")
        carrito = data.get("carrito")  # Lista de libros con ISBN y cantidad
        total = data.get("total")

        if not id_user or not carrito or total is None:
            return jsonify({"code": 1, "msg": "Datos incompletos"}), 400

        # Iniciar transacción en la base de datos
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                # Insertar venta
                cursor.execute(
                    "INSERT INTO venta (fec_ven, estado_ven, dni_lec) VALUES (NOW(), 1, %s)",
                    (id_user,)
                )
                id_venta = cursor.lastrowid

                # Insertar cada libro en venta_libro
                for item in carrito:
                    cursor.execute(
                        "INSERT INTO venta_libro (id_ven, isbn_lib, precio_ven) VALUES (%s, %s, %s)",
                        (id_venta, item["isbn_lib"], item["precio"])
                    )

            conexion.commit()

        return jsonify({"code": 0, "msg": "Venta guardada exitosamente"}), 201
    except Exception as e:
        return jsonify({"code": 1, "msg": f"Error al guardar la venta: {str(e)}"}), 500
