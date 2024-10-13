from flask import Blueprint, jsonify, request
from middleware.auth import authenticate_token

todos_bp = Blueprint("todos", __name__)

todos = []

@todos_bp.before_request
def before_request():
    authenticate_token()

# Endpoint 1: GET endpoint
@todos_bp.route("/", methods = ["GET"])
def get_todos():
    return jsonify(todos)

# Endpoint 2: Fetch a specific item by ID
@todos_bp.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    todo = next((t for t in todos if t["id"] == id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

# Endpoint 3: POST endpoint
@todos_bp.route("/", methods = ["POST"])
def create_todo():
    todo = {
        "id": len(todos) + 1,
        "title": request.json.get("title"),
        "completed": request.json.get("completed", False)
    }
    todos.append(todo)
    return jsonify(todo), 201


# Endpoint 4: PUT endpoint
@todos_bp.route("/<int:id>", methods = ["PUT"])
def update_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    todo['title'] = request.json.get("completed", todo['completed'])
    return jsonify(todo)
    

# Endpoint 5: DELETE endpoint
@todos_bp.route("/<int:id>", methods = ["DELETE"])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t['id'] != id]
    return '', 201