from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callback', methods=['GET'])
def callback():
    auth_code = request.args.get('code')
    state = request.args.get('state')
    return jsonify({"auth_code": auth_code, "state": state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
