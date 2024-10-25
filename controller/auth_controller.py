import services.lector_service as lector_service
import models.Lector as modelLector

def authenticate(email, password):
    try:
        lector = lector_service.obtener_lector(email)
        reader = modelLector.Lector(lector[0], lector[1], lector[2], lector[3], lector[4], lector[5], lector[6])
        if reader and reader.pws_lec == password:
            return reader
    except:
        return None
    
def identity(payload):
    try:
        lector_id = payload['identity']
        lector = lector_service.obtener_credenciales(lector_id)
        reader = modelLector.Lector(lector[0], lector[1], lector[2], lector[3], lector[4], lector[5], lector[6])
        return reader
    except:
        return None