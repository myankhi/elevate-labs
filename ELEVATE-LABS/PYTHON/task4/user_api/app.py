from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
users = {}

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to User API"}), 200

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

# GET single user
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404

# CREATE user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "id" not in data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    user_id = str(data["id"])
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400

    users[user_id] = {"name": data["name"]}
    return jsonify({"message": "User created", user_id: users[user_id]}), 201

# UPDATE user
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    if "name" not in data:
        return jsonify({"error": "Invalid data"}), 400

    users[user_id]["name"] = data["name"]
    return jsonify({"message": "User updated", user_id: users[user_id]}), 200

# DELETE user
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
