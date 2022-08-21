from flask import *

app=Flask(__name__)
app.debug=True

@app.route('/')
def hello():
    return 'Hello'
@app.route('/home')
def gethtml():
    return render_template('index.html')
#Query Strings
@app.route('/qs')
def qs():
    if request.args:
        req=request.args
        return " ".join(f"{k}:{v}" for k,v in req.items())
    return 'Bye Bye'


#HTTP Methos:  GET, POST, PUT, PATCH, DELETE and by default method is GET
order={
    "order1":{
        "Size":"Small",
        "Topping":"Cheese",
        "Crust":"Thin Crust"

    }
}
@app.route('/orders')
def orders():
      response=make_response(jsonify(order),200)
      return response

if __name__=='__main__':
    app.run()