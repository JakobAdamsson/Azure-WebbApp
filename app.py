from flask import Flask, jsonify
from markupsafe import escape
import requests
import json
app = Flask(__name__)
URL = 'https://lager.emilfolino.se/v2/products/everything'
# Use requests module to get JSON data
response = requests.get(URL)

# Turns response json object into a Dictionary
products_dict = response.json()
@app.route('/')
def hello():
    return 'test'
@app.route("/unique")
def remove_dups():
    
    #removing dups within product_dict
    no_dup_names = set([])
    stock_dict = {}
    for names in products_dict['data']:
        no_dup_names.add(names['name'].strip())
    for content in no_dup_names:
        stock_dict[content] = 0
    for contents in products_dict['data']:
        try:
            stock_dict[contents['name'].strip()] += contents['stock']
        except TypeError:
            pass
    new_products_dict = {'data': []}
    for key, amount in stock_dict.items():
        new_products_dict['data'].append({key: amount})
    return jsonify(stock_dict)

@app.route('/search/<product>')
def search_product(product):
    
    #removing dups within product_dict
    no_dup_names = set([])
    stock_dict = {}
    for names in products_dict['data']:
        no_dup_names.add(names['name'].strip())
    for content in no_dup_names:
        stock_dict[content] = 0
    for contents in products_dict['data']:
        try:
            stock_dict[contents['name'].strip()] += contents['stock']
        except TypeError:
            pass
    for key, amount in stock_dict.items():
        if product == key:
            product_exist = {'data': [{key: amount}]}
            return product_exist
    return 'Sorry finns ej kolla på byggmax istället'
