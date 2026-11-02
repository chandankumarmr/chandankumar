from flask import Flask,request,jsonify
import re

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')

    if not name:
       return jsonify({"error":"Name is required"}), 400
    
    if not email:
       return jsonify({"error":"Email is required"}), 400

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern,email):
       return jsonify({"error":"Invaild email format"}), 400

    return jsonify({
    "message":"Student registered successfully",
    "name":name,
    "email":email
    }), 200

if __name__ == '__main__':
   app.run(debug=True)