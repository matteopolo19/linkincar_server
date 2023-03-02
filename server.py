import json
from klein import Klein
from routes.autoscout import autoscout
from routes.automobile import automobile
from routes.subito import subito
from routes.json_makes_model import jsonMakes, jsonModel

app = Klein()

@app.route('/api')
def hello():
    return {"hello": "world"}

@app.route('/api/getAutoScout', methods=['GET'])
def autoscoutRoute(request):
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    return autoscout(request)

@app.route('/api/getAutomobile', methods=['GET'])
def automobileRoute(request):
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    return automobile(request)

@app.route('/api/getSubito', methods=['GET'])
def subitoRoute(request):
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    return subito(request)

@app.route('/api/getMakes', methods=['GET'])
def jsonMakesModelRoute(request):
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Access-Control-Allow-Methods', 'GET')
    request.setHeader('Access-Control-Allow-Headers', 'x-prototype-version,x-requested-with')
    brand = request.args.get(b'brand')
    if(brand is None):
        return jsonMakes()
    return jsonModel(brand[0].decode())

resource = app.resource