from flask import Flask, jsonify, request
import json
import ConectorMysql

app = Flask(__name__)

@app.route("/")
def ping():
        return jsonify({"response":"Bienvenido a la challenge API"})

@app.route('/postjson', methods = ['POST'])
def postJsonHandler():
    print ('Validate JSON Format')
    print (request.is_json)
    content = request.get_json()
    ip = json.dumps(content['IP'])
    proc = json.dumps(content['Procesador'])
    pscor = json.dumps(content['ProcesosCorriendo'])
    ucon = json.dumps(content['UsuariosConSesion'])
    so = json.dumps(content['NombreSO'])
    vso = json.dumps(content['VerSO'])
    ConectorMysql.abmbd(ip,proc,pscor,ucon,so,vso)
    return 'JSON posted'


if __name__ == '__main__':
        app.run(host="0.0.0.0", port=5000, debug=True)
