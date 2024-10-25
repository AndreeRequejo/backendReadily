class Lector(object):
    def __init__(self, dni_lec, nom_lec, apePat_lec, apeMat_lec, email_lec, pws_lec, fecha_nac):
        self.dni_lec = dni_lec
        self.nom_lec = nom_lec
        self.apePat_lec = apePat_lec
        self.apeMat_lec = apeMat_lec
        self.email_lec = email_lec
        self.pws_lec = pws_lec
        self.fecha_nac = fecha_nac

    def __str__(self):
        return f"Lector(dni_lec='{self.dni_lec}', email_lec='{self.email_lec}')"