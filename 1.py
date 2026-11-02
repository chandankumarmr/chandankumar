from flask import Flask,jsonify

app = Flask(__name__)

users = [
{"id":1,"name":"john","email":"john@gmail.com"}
,
{"id":2,"name":"Alice","email":"alice@gmail.com"}
,
{"id":3,"name":"Bob","email":"bob@gmail.com"}
,
{"id":4,"name":"David","email":"david@gmail.com"}
,
{"id":5,"name":"Emma","email":"emma@gmail.com"}
]
@app.route('/users',methods=['Get'])
def get_users():
  return jsonify(users)

@app.route('/users/<int:id>',methods=['Get'])
def get_user(id):
   for user in users:
     if user["id"] == id:
        return jsonify(user)

   return jsonify({"error":"user not found"}),404

if __name__ == '__main__':
   app.run(debug=True)
