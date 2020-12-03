from flask import Flask, jsonify, Response
from flask import request


from RecipeModel import *

from settings import *

import json
from bs4 import BeautifulSoup

import requests


def gettittle(variable):
    allrecipes = requests.get(variable)
    soup = BeautifulSoup(allrecipes.text, 'lxml')
    tittle = soup.h1
    hod = tittle.string
    return hod

# recipes to scrap
#


# get all recipes
nullvalue = "null"


@app.route('/recipes')
def get_recipes():
    return jsonify({'recipes': Recipe.get_all_recipes()})


@app.route('/recipes', methods=['POST'])
def add_recipe():
    recipe_data = request.get_json()
    print(recipe_data)
    idnGenerator = gettittle(str(recipe_data['URL'])) + "32"
    Recipe.add_recipes(_URL=recipe_data['URL'], _tittle=gettittle(
        str(recipe_data['URL'])), _time=nullvalue, _idn=idnGenerator)
    response = Response("", status=201, mimetype='application/json')
    response.headers['Location'] = "/recipes/" + str(idnGenerator)
    return response

# get recipe by idn and route it


@app.route('/recipes/<int:idn>')
def get_recipe_by_idn(idn):
    return_value = Recipe.get_recipe(idn)
    return jsonify(return_value)


# put request

@app.route('/recipes/<int:idn>', methods=['PUT'])
def replace_recipe(idn):
    request_data = request.get_json()
    Recipe.replace_recipe(idn, request_data['tittle'])
    return response


app.run(port=5000)
