import db.database as db
import random

def obtener_libro_completo():
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        li.isbn_lib, li.titulo_lib, li.anoPub_lib, li.estado_lib,
                        li.clasificacion, li.id_edi, li.bookPDF, li.image,
                        li.descripcion, li.calificacion_promedio, li.num_calificaciones,
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                        li.precio_lib
                    FROM libro li
                    INNER JOIN autor_libro al ON al.isbn_lib = li.isbn_lib
                    INNER JOIN autor au ON au.id_aut = al.id_aut
                """)
                libros = cursor.fetchall()

        return libros
    except Exception as e:
        print("Error al obtener libros:", e)
        return None

def obtener_libro_por_isbn(isbn_lib):
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                # Consulta para obtener un libro específico por isbn_lib
                cursor.execute("""
                    SELECT
                        li.isbn_lib, li.titulo_lib, li.anoPub_lib, li.estado_lib,
                        li.clasificacion, li.id_edi, li.bookPDF, li.image,
                        li.descripcion, li.calificacion_promedio, li.num_calificaciones,
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                        li.precio_lib
                    FROM libro li
                    INNER JOIN autor_libro al ON al.isbn_lib = li.isbn_lib
                    INNER JOIN autor au ON au.id_aut = al.id_aut
                    WHERE li.isbn_lib = %s
                """, (isbn_lib,))
                libro = cursor.fetchone()  # Obtén solo una fila

        return libro
    except Exception as e:
        print("Error al obtener el libro:", e)
        return None


def obtener_libros_comprados_por_usuario(email_user):
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT distinct
                        li.isbn_lib, li.titulo_lib, li.anoPub_lib, li.estado_lib,
                        li.clasificacion, li.id_edi, li.bookPDF, li.image,
                        li.descripcion, li.calificacion_promedio, li.num_calificaciones,
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                        li.precio_lib
                    FROM libro li
                    INNER JOIN autor_libro al ON al.isbn_lib = li.isbn_lib
                    INNER JOIN autor au ON au.id_aut = al.id_aut
                    INNER JOIN venta_libro vl ON vl.isbn_lib = li.isbn_lib
                    INNER JOIN venta v ON v.id_ven = vl.id_ven
                    INNER JOIN lector le ON le.dni_lec = v.dni_lec
                    INNER JOIN usuario usu ON usu.id_user = le.id_user
                    WHERE usu.email_user = %s
                """, (email_user,))

                libros_comprados = cursor.fetchall()

        return libros_comprados
    except Exception as e:
        print("Error al obtener libros comprados:", e)
        return None


def obtener_detalle_libro_por_isbn(isbn_lib):
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT isbn_lib, titulo_lib, bookPDF
                    FROM libro li
                    WHERE li.isbn_lib = %s
                """, (isbn_lib,))
                libro = cursor.fetchone()

        # Verifica si el libro existe
        if libro is None:
            return None

        # Convertir cualquier campo de tipo bytes a cadena
        libro = tuple(item.decode('utf-8') if isinstance(item, bytes) else item for item in libro)

        return libro
    except Exception as e:
        print("Error: ", e)
        return None



def obtener_libros_mas_vendidos():
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        l.isbn_lib, l.titulo_lib, l.anoPub_lib, l.estado_lib,
                        l.clasificacion, l.id_edi, l.bookPDF, l.image, l.descripcion,
                        l.calificacion_promedio, l.num_calificaciones,
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                        l.precio_lib
                    FROM venta_libro vl
                    JOIN libro l ON vl.isbn_lib = l.isbn_lib
                    JOIN autor_libro al ON l.isbn_lib = al.isbn_lib
                    JOIN autor au ON au.id_aut = al.id_aut
                    GROUP BY l.isbn_lib
                    ORDER BY COUNT(vl.id_ven) DESC
                    LIMIT 5
                """)
                libros = cursor.fetchall()

                # Si no hay libros vendidos, selecciona libros al azar
                if not libros:
                    cursor.execute("""
                        SELECT
                            l.isbn_lib, l.titulo_lib, l.anoPub_lib, l.estado_lib,
                            l.clasificacion, l.id_edi, l.bookPDF, l.image, l.descripcion,
                            l.calificacion_promedio, l.num_calificaciones,
                            CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                            l.precio_lib
                        FROM libro l
                        JOIN autor_libro al ON l.isbn_lib = al.isbn_lib
                        JOIN autor au ON au.id_aut = al.id_aut
                    """)
                    todos_los_libros = cursor.fetchall()

                    # Seleccionar libros al azar
                    cantidad_a_seleccionar = random.randint(5, 9)
                    libros = random.sample(todos_los_libros, min(cantidad_a_seleccionar, len(todos_los_libros)))

        return libros
    except Exception as e:
        print("Error: ", e)
        return None


def obtener_libros_antiguos():
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("""
                    SELECT
                        li.isbn_lib, li.titulo_lib, li.anoPub_lib, li.estado_lib,
                        li.clasificacion, li.id_edi, li.bookPDF, li.image, li.descripcion,
                        li.calificacion_promedio, li.num_calificaciones,
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo,
                        li.precio_lib
                    FROM libro li
                    JOIN autor_libro al ON li.isbn_lib = al.isbn_lib
                    JOIN autor au ON au.id_aut = al.id_aut
                    WHERE li.anoPub_lib < 2000
                """)
                libros = cursor.fetchall()
        return libros
    except Exception as e:
        print("Error: ", e)
        return None


def obtener_libros_actuales():
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                # Definimos como actuales los libros publicados desde el año 2000
                cursor.execute("""
                    SELECT
                        li.isbn_lib,            -- 0
                        li.titulo_lib,          -- 1
                        li.anoPub_lib,          -- 2
                        li.estado_lib,          -- 3
                        li.clasificacion,       -- 4
                        li.id_edi,              -- 5
                        li.bookPDF,             -- 6
                        li.image,               -- 7
                        li.descripcion,         -- 8
                        li.calificacion_promedio, -- 9
                        li.num_calificaciones,  -- 10
                        CONCAT(au.nom_aut, ' ', au.apePat_aut, ' ', au.apeMat_aut) AS nombre_completo, -- 11
                        li.precio_lib           -- 12
                    FROM libro li
                    INNER JOIN autor_libro al ON al.isbn_lib = li.isbn_lib
                    INNER JOIN autor au ON au.id_aut = al.id_aut
                    WHERE li.anoPub_lib >= 2000
                """)
                libros = cursor.fetchall()
        return libros
    except Exception as e:
        print("Error: ", e)
        return None


def obtener_libros_mejores_autores():
    try:
        with db.obtener_conexion() as conexion:
            with conexion.cursor() as cursor:
                # Consulta para obtener autores con más libros vendidos
                cursor.execute("""
                    SELECT a.id_aut, a.nom_aut, a.apePat_aut, a.apeMat_aut, COUNT(vl.id_ven) AS ventas
                    FROM autor a
                    JOIN autor_libro al ON a.id_aut = al.id_aut
                    JOIN venta_libro vl ON al.isbn_lib = vl.isbn_lib
                    GROUP BY a.id_aut
                    ORDER BY ventas DESC
                    LIMIT 5
                """)
                autores = cursor.fetchall()

                # Si no hay datos de ventas, selecciona autores al azar
                if not autores:
                    cursor.execute("SELECT id_aut, nom_aut, apePat_aut, apeMat_aut FROM autor")
                    todos_los_autores = cursor.fetchall()
                    cantidad_a_seleccionar = random.randint(5, 9)
                    autores = random.sample(todos_los_autores, min(cantidad_a_seleccionar, len(todos_los_autores)))

                # Obtener libros de estos autores
                autor_ids = [autor[0] for autor in autores]  # Cambia a índice numérico
                cursor.execute("""
                    SELECT
                        l.isbn_lib, l.titulo_lib, l.anoPub_lib, l.estado_lib,
                        l.clasificacion, l.id_edi, l.bookPDF, l.image, l.descripcion,
                        l.calificacion_promedio, l.num_calificaciones,
                        CONCAT(a.nom_aut, ' ', a.apePat_aut, ' ', a.apeMat_aut) AS nombre_completo,
                        l.precio_lib
                    FROM libro l
                    JOIN autor_libro al ON l.isbn_lib = al.isbn_lib
                    JOIN autor a ON al.id_aut = a.id_aut
                    WHERE a.id_aut IN %s
                """, (tuple(autor_ids),))
                libros = cursor.fetchall()

        return autores, libros
    except Exception as e:
        print("Error: ", e)
        return None, None

