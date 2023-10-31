from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<username>', methods=['GET'])
def get_user(username):
    user_data = {
        "username": username,
        "email": "alejo"
    }   
    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 200

@app.route("/update-user", methods=["PUT"])
def update_user():
    data = request.get_json()
    return jsonify(data), 200

@app.route("/delete-user", methods=["DELETE"])
def delete_user():
    return jsonify({"message": "User deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True, port=4000)