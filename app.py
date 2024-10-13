from flask import Flask, jsonify, request
from routes.todo import todos_bp

app = Flask(__name__)

app.register_blueprint(todos_bp, url_prefix = '/todos')


@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Resourse not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)