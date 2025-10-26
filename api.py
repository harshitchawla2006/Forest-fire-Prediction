# PUT and DELETE methods implementation in a Flask API
# working with JSON data
from flask import Flask, jsonify, request
app = Flask(__name__)

## initial data in TO DO LIST
items=[
    {"id":1,"name":"item1","description":"This is item 1"},
    {"id":2,"name":"item2","description":"This is item 2"},
]

@app.route('/')
def home():
    return "Welcome to the TO DO LIST API"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

## get: retrieve specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

## POST: create new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    
    # Validate required fields
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
    
    # Generate new ID
    new_id = max([item['id'] for item in items], default=0) + 1
    
    # Create new item
    new_item = {
        "id": new_id,
        "name": data['name'],
        "description": data.get('description', '')
    }
    
    items.append(new_item)
    return jsonify(new_item), 201

## PUT: update existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    
    # Update item fields
    if 'name' in data:
        item['name'] = data['name']
    if 'description' in data:
        item['description'] = data['description']
    
    return jsonify(item)

## DELETE: delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)