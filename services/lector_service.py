import db.database as db

def obtener_lector(email):
    try:
        conexion = db.obtener_conexion()
        lector = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT dni_lec, nom_lec, apePat_lec, apeMat_lec, email_lec, pws_lec, fecha_nac FROM lector WHERE email_lec = %s", (email,))
            lector = cursor.fetchone()
        conexion.close()
        return lector
    except Exception as e:
        print(repr(e))
        return None
    
def obtener_credenciales(dni):
    try:
        conexion = db.obtener_conexion()
        lector = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT dni_lec, nom_lec, apePat_lec, apeMat_lec, email_lec, pws_lec, fecha_nac FROM lector WHERE dni_lec = %s", (dni,))
            lector = cursor.fetchone()
        conexion.close()
        return lector
    except Exception as e:
        print(repr(e))
        return None