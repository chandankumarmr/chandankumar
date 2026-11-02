from flask import Flask, request, jsonify

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  
  username = data.get("username")
  password = data.get("password")

  if username == USERNAME and password == PASSWORD:
     return jsonify({
       "message": "LOGIN SUCCESSFUL"
     }), 200

  else:
    return jsonify({
      "message": "Invalid username or password"
    }), 401

if __name__ == '__main__':
    app.run(debug=True)

