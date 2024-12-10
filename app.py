from flask import Flask,jsonify
from flask_cors import flask_cors

app = Flask(__name__)
CORS(app)

products = [
    {
        "id":1,
        "name":"Harini",
        "price":34.00,
        "description":"pain relief and fever medication",
        "image_url":"https://via.placeholder.com/150"
    }
]

@app.route('/products',methods=['GET'])
def get_products():
    return jsonify(products)

if__name__=='__main__';
app.run(debug=True,host='http://127.0.0.1:5000')