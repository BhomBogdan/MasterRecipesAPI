from bs4 import BeautifulSoup

import requests

RecipeUrl = 'https://www.allrecipes.com/recipe/22281/black-bottom-cupcakes-ii/'


allrecipes = requests.get(RecipeUrl)

soup = BeautifulSoup(allrecipes.text, 'lxml')

tittle=soup.h1.string

URL = RecipeUrl

Time = soup.find_all(class_="recipe-meta-item-body")[2]

Time = Time.string
Time = Time.strip()


print(tittle)
print       
print(URL)
print
print(Time)



