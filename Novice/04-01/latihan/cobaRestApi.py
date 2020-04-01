from flask import Flask, Response
import json

app = Flask('Rest API')

@app.route('/')
def index():
    data ={
        "message": "Halo semuwa!! Selamat Datang di REST API keren ini."

    }

    data_json = json.dumps(data)
    return Response(data_json, mimetype='application/json')

app.run(debug=True)
