import platform
import socket
import json
import requests
import psutil

if __name__ == '__main__':
    # 1 direccion IP
    ip=socket.gethostbyname(socket.gethostname())

    # 2 Procesador
    procesador = platform.machine()
    # 3 Listado de procesos corriendo
    procesos = ''
    for p in psutil.process_iter():
        if(p.status()== 'running'):
            procesos = procesos + ' ' + p.name()
    # 4 usuarios con sesion abierta
    users = psutil.users()
    usuarios = ''
    for usr in users:
        usuarios = usuarios + ' ' + usr.name
    # 5 sistema operativo
    so = platform.system()
    # 6 Version sistema operativo
    version = platform.version()

    datos = {
        "IP":ip,
        "Procesador": procesador,
        "ProcesosCorriendo": procesos,
        "UsuariosConSesion": usuarios,
        "NombreSO": so,
        "VerSO": version
    }
    url = "http://0.0.0.0:5000/postjson"  

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    requests.post(url, data=json.dumps(datos), headers=headers)
