from flask import Flask, jsonify
from markupsafe import escape
import requests
import json
import random
app = Flask(__name__)
URL = 'https://lager.emilfolino.se/v2/products/everything'
# Use requests module to get JSON data
response = requests.get(URL)

# Turns response json object into a Dictionary
products_dict = response.json()
@app.route('/')
def hello():
    hello = """
    Välkommen - MENYVAL:
    
    1. För att visa sortimentet navigera till /unique
    
    
    2. För att söka på en specifik produkt navigera till /search/<din_produkt>
    
    
    3. För att kolla på reflektionen till kmom2 navigera till /ref
    
    """
    formatted_hello = hello.replace('\n', '<br>')
    return formatted_hello
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
    butiker = ['ByggMax', 'IcaMaxi', 'Coop', 'Apoteket', 'Partaj', 'Elgiganten', 'Logitech']
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
            return f'Produkten fanns ---> \n {product_exist}'
    return f'Sorry {product} finns inte, kolla på {butiker[random.randint(0,len(butiker)+1)]}'
