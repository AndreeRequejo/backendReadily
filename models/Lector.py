class Usuario(object):
    def __init__(self, dni_lec, nom_lec, apellidos_lec, fecha_nac):
        self.dni_lec = dni_lec
        self.nom_lec = nom_lec
        self.apellidos_lec = apellidos_lec
        self.fecha_nac = fecha_nac

    def __str__(self):
        return "Lector(dni='%s')" % self.dni_lec