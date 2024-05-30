from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

booked_slot = None  # Initialize booked_slot variable

@app.route('/log_button_id', methods=['POST'])
def log_button_id():
    global booked_slot  # Access the global booked_slot variable
    data = request.get_json()  # Get JSON data from request
    if data is None or 'button_id' not in data:
        return jsonify({'error': 'Invalid JSON or missing button_id'}), 400
    
    button_id = data['button_id']
    booked_slot = button_id  # Assign button_id to booked_slot
    # Process button_id as needed
    print("Clicked button ID:", button_id)

    return jsonify({'button_id': button_id}), 200

@app.route('/get_booked_slot', methods=['GET'])
def get_booked_slot():
    global booked_slot
    return jsonify({'booked_slot': booked_slot}), 200

@app.after_request
def print_booked_slot(response):
    global booked_slot
    # print("Clicked button ID:", booked_slot)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
