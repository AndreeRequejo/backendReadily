import db.database as db

def obtener_lector_id(dni):
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(
                    "SELECT dni_lec, nom_lec, apellidos_lec, fecha_nac, user_id FROM lector WHERE dni_lec = %s", (dni,))
                lector = cursor.fetchone()
        return lector
    except Exception as e:
        return None

def insertar_usuario(dni_lec, nom_lec, apellidos_lec, fecha_nac, user_id):
    try:
        conexion = db.obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuario (dni_lec, nom_lec, apellidos_lec, fecha_nac, user_id VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (dni_lec, nom_lec, apellidos_lec, fecha_nac, user_id))
        conexion.commit()
    except Exception as e:
        return None