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

@app.route('/ref')
def reflection():
    text = """
    Reflektion från frågorna om kmom2 - En applikation i molnet
    
    1. 
    
    2. Det som jag anser är så suveränt med JSON är att det är så lätt att skriva, lätt att läsa
    och det är väldigt lätt att ta en JSON fil som skapats i något annat programspråk för att använda det i 
    exempelvis Python. I detta kmom fick vi redan ett färdigt API där det direkt gick att använda med modulerna
    "Jsonify" och JSON. Det gick snabbt att konvertera JSON till en dictionary för att kunna jobba med den i Python.
    Hade det varit en databas som jag skulle jobba emot skulle det dels krävas förståelse kring databasen, men även
    modulerna som krävdes i Python för att kunna skriva och skicka över information till denna databasen.
    
    3. IAAS tjänster kräver att du har mer koll på dina saker då du behöver ha koll
    på bland annat datan och själva applikationen, men du behöver även ha koll på andra saker 
    så som ditt operativsystem och körtid. Medan PaaS kräver att du bara sköter om applikationen och datan,
    detta gör att det blir lättare för nybörjare att faktiskt få igång en fungerande webbapp
    
    4. Det främsta som jag kom att tänka på var simpliciteten, det är väldgt lätt att använda. Men det gör även att 
    jag som nybörjare inom detta kan fokusera på det viktiga och inte på att någon serverdator skulle krångla. Serverless arkitekturen
    är även generellt, från vad jag förstått, mycket säkert då man ofta använder svervrar av etablerade
    företag så som Google.
    
    5.
    
    6.
    
    7. Det jag tar med mig från detta kmom är hur JSON fungerar, även fast vi inte behövde lära oss jättemycket om JSON
    så valde jag att ta reda på lite mer om det. Jag har även lärt mig Flask, hur det fungerar och opererar och hur det inteagerar
    med Python. En annan viktig sak jag tar med mig är att det inte alltid är en dans på rosor, utan ibland stöter man på hinder och 
    då är det bara köra tills man hittar lösningen på sitt problem.
    """
    formated_text = text.replace('\n', '<br>')
    return formated_text