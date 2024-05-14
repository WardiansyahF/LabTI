from flask import Flask, request, jsonify

# Create a new Flask application instance
app = Flask(__name__)

# Predefined list of dictionaries representing stores and their items
datas = [
    {
        'id': 1,
        'name': 'Toko Bunga',
        'items': [
            {
                'name': 'Bunga Kecombrang',
                'price': 5000
            }
        ]
    }, {
        'id': 2,
        'name': 'Toko Buku',
        'items': [
            {
                'name': 'Buku Tangkuban Perahu',
                'price': 10000
            }
        ]
    }
]

# Define a route to get all stores
@app.route('/store')
def getAll():
    # Return all store data in JSON format
    return jsonify(datas)
# Define a route to get a store by its ID
@app.route('/store/<int:id>')
def getbyId(id):
    # Iterate through the stores to find the one with the matching ID
    for data in datas:
        if data['id'] == id:
            # Return the store data if found
            return jsonify(data)
    # Return an error message if the store is not found
    return jsonify({'message': 'Data not found'})

# Define a route to add a new store
@app.route('/store', methods=["POST"])
def addStore():
    # Get the data from the request body
    req_data = request.get_json()
    # Create a new store dictionary using the data from the request
    new_data = {
        'id': req_data['id'],
        'name': req_data['name'],
        'items': req_data['items']
    }
    # Add the new store to the list
    datas.append(new_data)
    # Return the newly added store data in JSON format
    return jsonify(new_data)

# Define the home route
@app.route('/')
def home():
    # Return a simple greeting message
    return "Hello peeps!"

# Check if the script is run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True)