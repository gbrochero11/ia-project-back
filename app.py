from flask import Flask, request, abort, make_response
from flask_cors import CORS

from sbr import SBR

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route("/api")
def hello_world():
    apiKey = request.headers.get('api-key')
    if (apiKey != 'e687be22a01996bf0ff4cafb741f8af2'):
        abort(401)
        return
    response = make_response("<p>Service UP</p>")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

@app.post('/api/sbr')
def sbr():

    apiKey = request.headers.get('api-key')
    if (apiKey != 'e687be22a01996bf0ff4cafb741f8af2'):
        abort(401)
        return 
    data = request.get_json()
    sbr = SBR(data=data)
    diagnostic = sbr.getDiagnostic();
    response = make_response(diagnostic)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response