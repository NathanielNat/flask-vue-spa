from flask import Flask, jsonify
from flask_cors import CORS

# configuration 
DEBUG = True

# initiating instance of app
app = Flask(__name__)
app.config.from_object(__name__)

#enable the CORS
CORS(app,resources={r'/*':{'origins':'*'}})

#sanity check route
@app.route('/ping',methods=['GET'])
def pinp_pong():
    return jsonify('pong')


if __name__ == '__main__':
    app.run()

