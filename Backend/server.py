from flask import Flask, jsonify, request
from flask_cors import CORS
import NumBaseConverter

app = Flask(__name__)
CORS(app)

@app.route('/api/v1.0/numBaseConvert', methods=['GET'])
def numBaseConvert():
    number = request.args.get('number')
    inputBase = int(request.args.get('inputBase'))
    outputBase = int(request.args.get('outputBase'))
    response = jsonify({'Output Number': NumBaseConverter.convertBase(number, inputBase, outputBase)})
    return response

if __name__ == '__main__':
    app.run(debug=True)