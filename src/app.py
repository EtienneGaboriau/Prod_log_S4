from libs.bottle import route, request, run, static_file
import json
from dao.Dao import *

#route pour permettre à la page html de charger le js
@route('/js')
def js_route():
    return static_file('script.js', root='./public/js')

#route qui donne les installation d'une ville
@route('/api/insta/<filepath:path>')
def insta_ville(filepath):
    nom, num = get_Installation(filepath)
    jsonObj = []
    for i in range(len(nom)):
        chaineJson = {"num" : str(num[i]), "name": nom[i]}
        jsonObj.append(chaineJson)
    return { "installations" : jsonObj }

#route home / accueil
@route('/')
def home():
    return static_file('index.html', root='./public', mimetype="text/html")

run(host='localhost', port=10078)
