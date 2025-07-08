from flask import Flask, request, jsonify

app = Flask(__name__)

# Define your API key
API_KEY = 'mysecretapikey123'

# Sample route with GET method and API key check
@app.route('/get-user', methods=['GET'])
def get_user():
    key = request.args.get('api_key')

    if key != API_KEY:
        return jsonify({'error': 'Unauthorized access'}), 401

    data = {
        'name': 'Nouman Aziz',
        'email': 'nouman@example.com'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
