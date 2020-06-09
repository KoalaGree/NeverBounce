#CREATED BY GONDRONG
#OJOK DI APAK2NO JANCOK
# 04 09 2020
import requests
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify


app = Flask(__name__)
api = Api(app)

class Bounce(Resource):
    def get(self, email):
        try:
            headers = {
            'authority': 'api.neverbounce.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'sec-fetch-user': '?1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
        }

            params = (
                ('key', 'private_22c0091eb1c3d8acc8776ea2ea6d2a5e'),
                ('email', email),
        )

            response = requests.get('https://api.neverbounce.com/v4/single/check', headers=headers, params=params)
            data = response.json()
            #print (response.text)
            if response.status_code == 200:
                stat = data['result']
                if stat == 'valid':
                    return 'Live'
                elif stat == 'invalid':
                    return 'Die'
        except:
            return 'Unknown'


api.add_resource(Bounce, '/Bounce/<email>') # Route_3

if __name__ == "__main__":
    app.run(debug=True)