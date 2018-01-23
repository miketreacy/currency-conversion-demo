from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/hello')
def hello():
    """Simple example of an API endpoint"""
    return jsonify({'message': 'ohai'})


@app.route('/hello/<string:name>')
def hello_name(name):
    """Simple example using an URL parameter"""
    return jsonify({'message': 'ohai {}'.format(name)})


@app.route('/rate/<string:currency1>/to/<string:currency2>')
def rate_conversion(currency1, currency2):
    params = {'base': currency1, 'symbols': currency2}
    res = requests.get('https://api.fixer.io/latest', params=params)
    data = res.json()
    return jsonify(
        {
            'from': '{}'.format(currency1),
            'to': '{}'.format(currency2),
            'rate': '{}'.format(data['rates'][currency2])
        })


@app.route('/convert/<string:currency1>/<string:amount>/to/<string:currency2>')
def amount_conversion(currency1, currency2, amount):
    params = {'base': currency1, 'symbols': currency2}
    res = requests.get('https://api.fixer.io/latest', params=params)
    data = res.json()
    rate = data['rates'][currency2]
    return jsonify(
        {
            'from': '{}'.format(currency1),
            'from_amount': float(amount),
            'to': '{}'.format(currency2),
            'converted_amount': '{:.2f}'.format(float(amount) * float(rate))
        })
