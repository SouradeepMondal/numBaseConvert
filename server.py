from flask import Flask, jsonify, request
import NumBaseConverter

app = Flask(__name__)

@app.route('/api/v1.0/numBaseConvert', methods=['GET'])
def numBaseConvert():
    number = request.args.get('number')
    inputBase = int(request.args.get('inputBase'))
    outputBase = int(request.args.get('outputBase'))
    return jsonify({'Output Number': NumBaseConverter.convertBase(number, inputBase, outputBase)})

if __name__ == '__main__':
    app.run(debug=True)