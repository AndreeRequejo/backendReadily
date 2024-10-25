import pymysql

'''def obtener_conexion():
    return pymysql.connect(host='GrupoMobiles01.mysql.pythonanywhere-services.com',
                                user='GrupoMobiles01',
                                password='android24',
                                db='GrupoMobiles01$libreria')'''

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='1234',
                                db='readily')