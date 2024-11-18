# Modelo del carrito (opcional)
class Carrito(object):
    def __init__(self, id_user, isbn_lib, cantidad):
        self.id_user = id_user
        self.isbn_lib = isbn_lib
        self.cantidad = cantidad

    def json(self):
        return {
            "id_user": self.id_user,
            "isbn_lib": self.isbn_lib,
            "cantidad": self.cantidad
        }
