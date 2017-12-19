#!/usr/bin/env python
# import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

import fix_yahoo_finance as yf

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "price.check":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    stock = parameters.get("price_check")

    cost = {'chevron': 'cvx', 'Exxon': 'XOM', 'BP': 'BP', 'TOTAL': 'TOT', 'oil':'CLF18.NYM'}
    price = yf.download(cost[stock])

    speech = "The price of " + stock + " is " + str(round(price['Close'][-1])) + " dollar."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "Oili"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
