import services.usuario_service as usuario_service
import models.Usuario as modelUsuario

def authenticate(username, password):
    try:
        usuario = usuario_service.obtener_usuario(username)
        user = modelUsuario.Usuario(usuario[0], username, usuario[2])
        if user and user.pws_lec == password:
            return user
    except:
        return None
    
def identity(payload):
    try:
        user_id = payload['identity']
        usuario = usuario_service.obtener_credenciales(user_id)
        user = modelUsuario.Usuario(user_id, usuario[1], usuario[2])
        return user
    except:
        return None