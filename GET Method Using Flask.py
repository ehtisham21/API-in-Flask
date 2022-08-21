from flask import *

app=Flask(__name__)
app.debug=True

orders={
    "order1": {
        "Size": "Small",
        "Topping": "Cheese",
        "Crust": "Thin Crust"
    },
    "order2": {
        "Size": "Small",
        "Topping": "Cheese",
    },
    "order3": {
        "Size": "Small",
        "Crust": "Thin Crust"
    },
    "order4": {
        "Size": "Large",
        "Topping": "Cheese",
        "Crust": "Thin Crust"
    },
    "order5": {
        "Size": "Small",
        "Topping": "Extra",
        "Crust": "Thick Crust"
    }
}

@app.route('/orders')
def ordersdetails():
    resp=make_response(jsonify(orders),200)
    return resp
@app.route('/orders/<orderid>')
def selectorderid(orderid):
    if orderid in orders:
        resp=make_response(jsonify(orders[orderid]),200)
        return resp
    else:
        return "Your Entered Wrong Order ID"
@app.route('/orders/<orderid>/<items>')
def selectorderdetails(orderid,items):
    items=orders[orderid].get(items)
    if items:
        respo=make_response(jsonify(items),200)
        return respo
    else:
        return "Your Entered Wrong Order Details"
@app.route('/')
def home():
    return "This is Home Page"
if __name__=='__main__':
    app.run()