import hashlib
import hmac
import requests
from flask import Flask, request, render_template
from pip._internal.utils import logging

logger = logging.getLogger(__name__)


app = Flask(__name__, static_folder="static", static_url_path='', template_folder='templates')

@app.route('/order', methods=['GET'])
def create_order():
    DATA = {
        "amount": 500000,
        "currency": "INR",
        "payment_capture": 1
    }
    key_id = "" # Enter your API_key
    key_secret = "" # enter the key_secret
    response = requests.post("https://{}:{}@api.razorpay.com/v1/orders?"
                             "amount={}&currency={}&payment_capture={}".format(key_id, key_secret, DATA.get('amount'),
                                                                               DATA.get('currency'),
                                                                               DATA.get('payment_capture')),
                                                                               verify=False).json()
    order_id = response.get('id', None)
    currency = response.get('currency', None)
    amount = response.get('amount', None)
    return render_template('app.js', amount=amount, currency=currency, order_id=order_id, key_id=key_id)


@app.route('/charge', methods=['POST'])
def app_charge():
    key_secret = ""  # enter the key_secret
    payment_id = request.form['razorpay_payment_id']
    order_id = request.form['razorpay_order_id']
    signature = request.form['razorpay_signature']
    parameters = {
        "razorpay_order_id": order_id,
        "razorpay_payment_id": payment_id,
        "razorpay_signature": signature
    }
    msg = "{}|{}".format(str(parameters.get('razorpay_order_id')), str(parameters.get('razorpay_payment_id')))

    secret = str(key_secret)

    key = bytes(secret, 'utf-8')
    body = bytes(msg, 'utf-8')

    dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

    generated_signature = dig.hexdigest()
    result = hmac.compare_digest(generated_signature, signature)
    if result == True:
        return render_template("thankyou.html")
    else:
        raise logger

if __name__ == '__main__':
    app.run()