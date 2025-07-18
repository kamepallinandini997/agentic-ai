from flask import Flask, request, jsonify
import os, json, logging
from datetime import datetime

DATA_FILE = "users.json"

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

app = Flask(__name__)

@app.route("/user/register", methods=["POST"])
def register_user():
    try:
        data = request.get_json()
        app.logger.info(f"Data received from user: {data}")
        
        # check if username is sent by request
        new_username = data.get("username")
        if not new_username:
            return jsonify([{"Message": "Username is required"}]), 400

        users = load_from_json()
        for user in users:
            if user["username"] == new_username:
                return jsonify([{"Message": "User ID already exists. Try logging in."}]), 409

        users.append(data)
        save_to_json(users)
        return jsonify([{"Message": "User Registered Successfully", "Code": "200"}]), 200

    except Exception as e:
        app.logger.error(f"Exception in registration: {e}")
        return jsonify([{"Message": "Internal Server Error"}]), 500

@app.route("/user/login", methods=["POST"])       
def login():
    try:
        data = request.get_json()
        app.logger.info(f"Login attempt: {data}")
        
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify([{"Message": "Username and password are required"}]), 400

        users = load_from_json()
        for user in users:
            if user["username"] == username and user["password"] == password:
                return jsonify([{"Message": "Login successful", "Code": "200"}]), 200
        
        return jsonify([{"Message": "Invalid username or password"}]), 401

    except Exception as e:
        app.logger.error(f"Exception in login: {e}")
        return jsonify([{"Message": "Internal Server Error"}]), 500
from datetime import datetime

@app.route("/user/verify-age", methods=["GET"])
def verify_user_ages():
    try:
        users = load_from_json()
        marked_users = []

        for user in users:
            dob_str = user.get("dob")
            provided_age = user.get("age")

            if not dob_str or not provided_age:
                continue  # Skip if missing data

            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d")  # Assumes dob format is YYYY-MM-DD
                today = datetime.today()
                calculated_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            except Exception as e:
                app.logger.warning(f"Error parsing dob for user {user.get('username')}: {e}")
                continue

            if int(provided_age) != calculated_age:
                user["marked"] = True
                marked_users.append(user)

        return jsonify(marked_users), 200

    except Exception as e:
        app.logger.error(f"Exception in age verification: {e}")
        return jsonify([{"Message": "Internal Server Error"}]), 500


def load_from_json():
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            app.logger.info("Loading data from JSON file")
            return json.load(f)
    except Exception as e:
        app.logger.error(f"Error loading JSON: {e}")
        return []

def save_to_json(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        app.logger.error(f"Error saving JSON: {e}")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
