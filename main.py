from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('','index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return send_from_directory('', 'about.html')

@app.route('/buy.html', methods = ['GET'])
def buy_data():
    return send_from_directory('', 'buy.html')

@app.route('/subscribe/<name>/<email>', methods=['POST'])
def subscribe(name, email):
    # write data to database
    pass


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    # wallet = Wallet(port)
    # blockchain = Blockchain(wallet.public_key, port)
    app.run(host='0.0.0.0', port=port, debug = True)
