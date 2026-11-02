from flask import Flask, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/addOrders', methods=['post'])
def add_order():
  data = request.get_json()

  order = {
    "id":len(orders) + 1,
    "user": data["user"],
    "product": data["product"],
    "quantity": data["quantity"],
    "price": data["price"],
    "total": data["quantity"] * data["price"]
    }
 
  orders.append(order)
  return jsonify({
    "message": "Order added successfully",
    "order": order
  }), 201

@app.route('/showOrders', methods=['GET'])
def show_orders():
  return jsonify({
     "message": "Recent Orders",
     "orders": orders[::-1]
  })

if __name__ == '__main__':
   app.run(debug=True)